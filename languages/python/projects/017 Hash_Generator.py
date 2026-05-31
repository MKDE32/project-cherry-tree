import hashlib



def generate_hashes(text: str):
    data = text.encode()

    hashes = {
        "MD5": hashlib.md5(data).hexdigest(),
        "SHA1": hashlib.sha1(data).hexdigest(),
        "SHA256": hashlib.sha256(data).hexdigest(),
    }

    return hashes



def main():
    print("=== Hash Generator (MD5 / SHA1 / SHA256) ===\n")

    text = input("Passwort: ")

    use_salt = input("Salt verwenden? (y/n): ").strip().lower()
    if use_salt == "y":
        salt = input("Salt-Wert: ")
        position = input("Salt-Position (prefix/suffix): ").strip().lower()

        if position == "prefix":
            text = salt + text
        elif position == "suffix":
            text = text + salt
        else:
            print("Ungültige Salt-Position")
            return

    print("\nHashes:\n")
    hashes = generate_hashes(text)
    for algo, value in hashes.items():
        print(f"{algo:<7}: {value}")

if __name__ == "__main__":
    main()













