import hashlib
import sys
import time



def hash_password(password: str, algo: str) -> str:
    password = password.encode()
    if algo == "md5":
        return hashlib.md5(password).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(password).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(password).hexdigest()
    else:
        raise ValueError("Unbekannter Hash-Typ")



def crack_hash(
    target_hash: str,
    wordlist_path: str,
    algo: str,
    salt: str = "",
    salt_position: str = "none"
):
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            words = f.readlines()
    except FileNotFoundError:
        print("Wordlist not found")
        sys.exit(1)

    total = len(words)
    print(f"Starte Crack-Versuch ({algo.upper()})")
    print(f"Wordlist: {total} Einträge")
    print(f"Salt: '{salt}' ({salt_position})\n")

    start_time = time.time()

    for i, word in enumerate(words, start=1):
        word = word.strip()

        if salt_position == "prefix":
            test_pw = salt + word
        elif salt_position == "suffix":
            test_pw = word + salt
        else:
            test_pw = word

        hashed = hash_password(test_pw, algo)

        if hashed == target_hash:
            duration = time.time() - start_time
            print("\n PASSWORT GEFUNDEN!")
            print(f"Passwort: {word}")
            print(f"Zeit: {duration:2f} Sekunden")
            return

        if i % 1000 == 0 or i == total:
            percent = (i / total) *100
            sys.stdout.write(
                f"\r Fortschritt: {i}/{total} ({percent:2f}%)"
            )
            sys.stdout.flush()

    print("\n Passwort nicht in Wordlist gefunden")



if __name__ == "__main__":
    print("=== CTF Hash Cracker ===\n")

    target_hash = input("Ziel Hash: ").strip().lower()
    algo = input("Hash-Typ (md5/sha1/sha256): ").strip().lower()
    wordlist = input("Pfad zur Wordlist: ").strip()

    use_salt = input("Salt verwenden? (y/n): ").strip().lower()
    salt = ""
    salt_position = "none"

    if use_salt == "y":
        salt = input("Salt-Wert: ").strip()
        salt_position = input("Salt-Position (prefix/suffix): ").strip().lower()

    crack_hash(target_hash, wordlist, algo, salt, salt_position)










