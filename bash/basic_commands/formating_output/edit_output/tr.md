# example
```
cat /etc/passwd | tr ":" " "
tr -d '[:digit:]'
```
- ersetzt : durch leerzeichen in der ausgabe
- remove digits


# flags

| Option      | Type | Purpose                    | Typical Use                               |
| ----------- | ---- | -------------------------- | ----------------------------------------- |
| `-d`        | flag | Delete characters          | Remove unwanted chars (e.g. `\r`, digits) |
| `-s`        | flag | Squeeze repeats            | Collapse repeated chars (`///` → `/`)     |
| `-c`        | flag | Complement set             | Operate on *everything except* set        |
| `-C`        | flag | Same as `-c` (BSD variant) | Compatibility mode                        |
| `--help`    | flag | Show help                  | Quick reference                           |
| `--version` | flag | Show version               | Debug environment                         |

| Class       | Meaning            |
| ----------- | ------------------ |
| `[:lower:]` | lowercase letters  |
| `[:upper:]` | uppercase letters  |
| `[:alpha:]` | letters            |
| `[:digit:]` | numbers            |
| `[:alnum:]` | letters + numbers  |
| `[:space:]` | whitespace         |
| `[:punct:]` | punctuation        |
| `[:cntrl:]` | control characters |


















