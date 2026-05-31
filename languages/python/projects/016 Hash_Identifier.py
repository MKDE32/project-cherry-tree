import re

def identify_hash(hash_value: str):
    hash_value = hash_value.strip().lower()
    results = []

    patterns = [
        ("MD5", re.fullmatch(r"[a-f0-9]{32}", hash_value)),
        ("SHA1", re.fullmatch(r"[a-f0-9]{40}", hash_value)),
        ("SHA256", re.fullmatch(r"[a-f0-9]{64}", hash_value)),
        ("SHA512", re.fullmatch(r"[a-f0-9]{128}", hash_value)),
        ("bcrypt", hash_value.startswith("$2a$") or hash_value.startswith("$2b$")),
        ("MD5 (Unix)", hash_value.startswith("$1$")),
        ("SHA256 (Unix)", hash_value.startswith("$5$")),
        ("SHA512 (Unix)", hash_value.startswith("$6$")),
    ]

    for name, match in patterns:
        if match:
            results.append(name)

    return results


def main():
    print("=== Hash Identifier ===\n")

    hash_value = input("🔑 Hash eingeben: ")

    matches = identify_hash(hash_value)

    if matches:
        print("\n🧠 Mögliche Hash-Typen:")
        for h in matches:
            print(f" - {h}")
    else:
        print("\n❌ Unbekannter oder nicht unterstützter Hash-Typ")


if __name__ == "__main__":
    main()
