| Format              | Example Command                               |
| ------------------- | --------------------------------------------- |
| NetNTLMv2           | `john --format=netntlmv2 hashes.txt`          |
| Kerberos 5 TGS-REP  | `john --format=krb5tgs hashes.txt`            |
| Kerberos 5 AS-REP   | `john --format=krb5asrep hashes.txt`          |
| Raw SHA-256         | `john --format=raw-sha256 hashes.txt`         |
| Raw SHA-512         | `john --format=raw-sha512 hashes.txt`         |
| PBKDF2-HMAC-SHA256  | `john --format=pbkdf2-hmac-sha256 hashes.txt` |
| LM (legacy Windows) | `john --format=LM hashes.txt`                 |
| DES crypt           | `john --format=descrypt hashes.txt`           |
