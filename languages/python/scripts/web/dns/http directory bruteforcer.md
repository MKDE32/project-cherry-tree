```python
import requests
import sys
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

lock = Lock()
progress_counter = 0


def check_path(url, timeout=5):
    try:
        r = requests.get(url, timeout=timeout)
        if r.status_code in [200, 301, 302, 403]:
            return f"[{r.status_code}] {url}"
    except requests.RequestException:
        pass
    return None


def dir_bruteforce(base_url, wordlist_path, extensions, threads):
    global progress_counter

    wordlist = Path(wordlist_path)

    if not wordlist.exists():
        print("❌ Wordlist nicht gefunden")
        sys.exit(1)

    with wordlist.open("r", errors="ignore") as f:
        words = [line.strip() for line in f if line.strip()]

    urls = [
        f"{base_url.rstrip('/')}/{word}{ext}"
        for word in words
        for ext in extensions
        if not word.startswith("#")
    ]

    total = len(urls)

    print(f"\n🔍 Ziel: {base_url}")
    print(f"📄 URLs gesamt: {total}")
    print(f"🧵 Threads: {threads}")
    print(f"📦 Extensions: {', '.join(extensions) if extensions else 'keine'}\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(check_path, url) for url in urls]

        for future in as_completed(futures):
            result = future.result()

            with lock:
                progress_counter += 1
                percent = (progress_counter / total) * 100
                print(f"\r⏳ Fortschritt: {percent:6.2f}%", end="")

            if result:
                print(f"\n{result}")

    print("\n\n✅ Scan abgeschlossen")


def main():
    parser = argparse.ArgumentParser(description="Simple Directory Bruteforcer")

    parser.add_argument("url", help="Ziel-URL (z.B. http://example.com)")
    parser.add_argument("wordlist", help="Pfad zur Wordlist")

    parser.add_argument(
        "-t", "--threads",
        type=int,
        default=20,
        help="Anzahl Threads (Default: 20)"
    )

    parser.add_argument(
        "-x", "--extensions",
        default="",
        help="Dateiendungen, z.B. php,html,txt"
    )

    args = parser.parse_args()

    extensions = [""]
    if args.extensions:
        extensions += [f".{ext.strip()}" for ext in args.extensions.split(",")]

    dir_bruteforce(
        base_url=args.url,
        wordlist_path=args.wordlist,
        extensions=extensions,
        threads=args.threads
    )


if __name__ == "__main__":
    main()

```
