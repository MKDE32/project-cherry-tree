| `-m` ID | Algorithm              | Typical Use Case                        |
| ------- | ---------------------- | --------------------------------------- |
| `0`     | MD5                    | Legacy apps, simple web hashes          |
| `100`   | SHA1                   | Older systems, git, legacy APIs         |
| `900`   | MD4                    | NTLM foundation, legacy protocols       |
| `1000`  | NTLM                   | Windows password hashes                 |
| `1800`  | sha512crypt            | Linux `/etc/shadow` (modern distros)    |
| `1400`  | SHA256                 | General-purpose hashing                 |
| `1700`  | SHA512                 | General-purpose / Linux variants        |
| `500`   | md5crypt               | Older Unix systems                      |
| `3000`  | LM                     | Very old Windows hashes (weak)          |
| `5500`  | NetNTLMv1              | Network authentication (legacy Windows) |
| `5600`  | NetNTLMv2              | Modern Windows network auth             |
| `1500`  | descrypt               | Legacy Unix crypt                       |
| `10000` | Django (PBKDF2-SHA256) | Web frameworks                          |
| `10900` | PBKDF2-HMAC-SHA256     | Modern application auth                 |
