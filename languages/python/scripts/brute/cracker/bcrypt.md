import bcrypt
from pathlib import Path
from tqdm import tqdm

def load_wordlist():
    base_dir = Path(__file__).parent
    wordlist_file = base_dir / "wordlist.txt"

    if not wordlist_file.exists():
        print(f"[-] Keine wordlist.txt gefunden in {base_dir}")
        return []

    with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]


def crack_bcrypt(target_hash):
    target_hash = target_hash.encode('utf-8')

    print("[*] Starte bcrypt Wordlist-Check")
    print(f"[*] Target: {target_hash.decode()[:30]}...")
    print("-" * 50)

    passwords = load_wordlist()

    if not passwords:
        print("[-] Wordlist ist leer oder fehlt.")
        return None

    print(f"[*] Wordlist geladen: {len(passwords)} Einträge")

    # 🔥 Fortschrittsbalken
    for pw in tqdm(passwords, desc="Cracking", unit="pw"):
        pw_bytes = pw.encode('utf-8')

        if bcrypt.checkpw(pw_bytes, target_hash):
            print(f"\n[+] PASSWORT GEFUNDEN: {pw}")
            return pw

    print("\n[-] Nicht gefunden")
    return None


if __name__ == "__main__":
    target = input("Hash: ").strip()
    crack_bcrypt(target)
