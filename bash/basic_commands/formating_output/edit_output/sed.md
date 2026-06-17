# examples
```
sed 's/foo/bar/' file.txt
cat f | sed 's/5/X/g'
```
- Ersetzen von Text in einer Datei
- substituting text. ersetzt jede 5 durch X



| Flag          | Type   | Purpose                       | Typical Use                           |
| ------------- | ------ | ----------------------------- | ------------------------------------- |
| `-e <script>` | option | Adds a sed script to execute  | Multiple expressions inline           |
| `-f <file>`   | option | Reads sed commands from file  | Reusable transformations              |
| `-i[SUFFIX]`  | option | In-place editing of files     | Direct file modification              |
| `-n`          | option | Suppresses automatic printing | Used with `p` command                 |
| `-r` / `-E`   | option | Extended regex mode           | Cleaner regex syntax                  |
| `-s`          | option | Treat files separately        | Multi-file behavior control (GNU sed) |
| `-u`          | option | Unbuffered output             | Streaming/log processing              |
| `--posix`     | option | Strict POSIX compliance       | Portability                           |
| `--debug`     | option | Debug execution flow          | Script troubleshooting                |



| Construct    | Type     | Purpose                  | Example                      |
| ------------ | -------- | ------------------------ | ---------------------------- |
| `s/old/new/` | command  | Substitution             | Replace text                 |
| `g`          | modifier | Global replacement       | Replace all matches per line |
| `p`          | command  | Print pattern space      | Used with `-n`               |
| `d`          | command  | Delete lines             | Filter output                |
| `q`          | command  | Quit early               | Performance optimization     |
| `a\text`     | command  | Append line after match  | Insert output                |
| `i\text`     | command  | Insert line before match | Prepend content              |
| `c\text`     | command  | Change entire line       | Replace full line            |
| `y/abc/xyz/` | command  | Transliterate chars      | Simple encoding transforms   |










