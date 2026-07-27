from multiprocessing import Pool, cpu_count
from tqdm import tqdm
import bcrypt


def check_password(args):
    password, target_hash = args
    password_bytes = password.encode("utf-8")

    if bcrypt.checkpw(password_bytes, target_hash):
        return password
    return None


def crack_parallel(target_hash, passwords):
    target_hash_bytes = target_hash.encode("utf-8")

    processes = max(1, cpu_count() - 2)

    print(f"[*] Starte mit {processes} Prozessen")
    print(f"[*] Wordlist: {len(passwords)} Einträge")

    total = len(passwords)

    with Pool(processes) as pool:
        found = None

        for result in tqdm(
            pool.imap_unordered(
                check_password,
                [(pw, target_hash_bytes) for pw in passwords]
            ),
            total=total,
            desc="Cracking"
        ):
            if result:
                found = result
                break

    if found:
        print(f"\n[+] PASSWORT GEFUNDEN: {found}")
    else:
        print("\n[-] Passwort nicht gefunden")

    return found


def load_wordlist(wordlist_path):
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]


def main():
    print("=== bcrypt parallel cracker ===")

    target_hash = input("Hash: ").strip()
    wordlist_path = input("Wordlist: ").strip()
    wordlist = load_wordlist(wordlist_path)
    crack_parallel(target_hash, wordlist)


if __name__ == "__main__":
    main()
