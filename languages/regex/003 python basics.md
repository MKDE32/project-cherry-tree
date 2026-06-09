# re modul
```
import re

re.search(pattern, text)      # erstes Vorkommen
re.findall(pattern, text)    # alle Treffer als Liste
re.sub(pattern, neu, text)   # ersetzen
re.match(pattern, text)      # nur am Stringanfang
```
# strings
| Regex | Bedeutung                       | Beispiel | Match        |
| ----- | ------------------------------- | -------- | ------------ |
| `.`   | Beliebiges Zeichen (außer `\n`) | `a.c`    | `abc`, `a7c` |
| `\d`  | Ziffer                          | `\d+`    | `123`        |
| `\D`  | Keine Ziffer                    | `\D+`    | `abc`        |
| `\w`  | Buchstabe, Zahl, `_`            | `\w+`    | `abc_123`    |
| `\W`  | Kein Buchstabe/Zahl/_           | `\W+`    | `!?@`        |
| `\s`  | Leerzeichen, Tab, Zeilenumbruch | `\s+`    | `"   "`      |
| `\S`  | Kein Leerzeichen                | `\S+`    | `hello`      |

# repeat
| Regex   | Bedeutung        | Beispiel  |
| ------- | ---------------- | --------- |
| `*`     | 0 oder mehr      | `ab*c`    |
| `+`     | 1 oder mehr      | `ab+c`    |
| `?`     | 0 oder 1         | `https?`  |
| `{3}`   | Genau 3-mal      | `\d{3}`   |
| `{2,5}` | 2 bis 5-mal      | `\w{2,5}` |
| `{2,}`  | Mindestens 2-mal | `a{2,}`   |



| Regex         | Bedeutung         |
| ------------- | ----------------- |
| `[abc]`       | a oder b oder c   |
| `[a-z]`       | Kleinbuchstaben   |
| `[A-Z]`       | Großbuchstaben    |
| `[0-9]`       | Ziffern           |
| `[a-zA-Z0-9]` | Alphanumerisch    |
| `[^abc]`      | Alles außer a,b,c |
| `[^"]+`       | Alles außer `"`   |








































































