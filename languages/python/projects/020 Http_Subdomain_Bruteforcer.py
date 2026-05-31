import requests
import sys
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

lock = Lock()
progress_counter = 0


def check_subdomains(subdomain, timeout=5):
    url = f"http://{subdomain}"
    try:
        r = requests.get(url, timeout=timeout)
        return f"[{r.status_code}] {subdomain}"
    except requests.RequestException:
        return None


def subdomain_bruteforce(domain, wordlist_path, threads):
    global progress_counter

    wordlist = Path(wordlist_path)

    if not wordlist.exists():
        print("❌ Wordlist nicht gefunden")
        sys.exit(1)

    with wordlist.open("r", errors="ignore") as f:
        words = [line.strip() for line in f if line.strip()]

    subdomains = [
        f"{word}.{domain}"
        for word in words
        if not word.startswith("#")
    ]

    total = len(subdomains)

    print(f"\n🔍 Ziel: {domain}")
    print(f"📄 URLs gesamt: {total}")
    print(f"🧵 Threads: {threads}\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(check_subdomains, sub) for sub in subdomains]

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
    parser = argparse.ArgumentParser(description="Simple Subdomain Bruteforcer")

    parser.add_argument("domain", help="Ziel-URL (z.B. http://example.com)")
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

    subdomain_bruteforce(
        domain=args.domain,
        wordlist_path=args.wordlist,
        threads=args.threads
    )


if __name__ == "__main__":
    main()
