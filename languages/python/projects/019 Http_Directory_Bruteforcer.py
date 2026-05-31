# pip install requests



import requests
import sys
from pathlib import Path



def dir_bruteforce(
    base_url: str,
    wordlist_path: str,
    extensions=None,
    timeout=5
):
    if extensions is None:
        extensions = [""]

    wordlist = Path(wordlist_path)

    if not wordlist.exists():
        print("Wordlist nicht gefunden")
        sys.exit(1)

    with wordlist.open("r", errors="ignore") as f:
        words = [line.strip() for line in f if line.strip()]

    total = len(words) * len(extensions)
    count = 0

    print(f"Starte Scan auf {base_url}")
    print(f"Einträge: {total}\n")

    for word in words:
        for ext in extensions:
            count += 1
            path = f"{word}{ext}"
            url = f"{base_url.rstrip('/')}/{path}"

            try:
                r = requests.get(url, timeout=timeout)

                if r.status_code in [200, 301, 302, 400]:
                    print(f"[{r.status_code}] {url}")

            except requests.RequestException:
                pass

            if count % 100 == 0:
                print(f"Progress: {count}/{total}")

    print("\nScan beendet")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage:")
        print("python3 Http_Directory_Bruteforcer.py http://target wordlist.txt")
        sys.exit(1)

    base_url = sys.argv[1]
    wordlist_path = sys.argv[2]

    extensions = ["", ".php", "html", ".txt"]

    dir_bruteforce(base_url, wordlist_path, extensions)















