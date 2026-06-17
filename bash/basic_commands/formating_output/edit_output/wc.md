zählt die zeilen
```
find /etc/ -name *.conf 2>/dev/null | grep systemd | wc -l
```


zählt die buchstaben
```
cat f | wc -c
```

# flags
| Option                 | Type   | Purpose                      | Typical Use                       |
| ---------------------- | ------ | ---------------------------- | --------------------------------- |
| `-l`                   | flag   | Count lines                  | File size in lines / log entries  |
| `-w`                   | flag   | Count words                  | Text analysis / NLP preprocessing |
| `-c`                   | flag   | Count bytes                  | File size in bytes                |
| `-m`                   | flag   | Count characters             | Unicode-aware text length         |
| `-L`                   | flag   | Show longest line length     | Format diagnostics                |
| `--files0-from=<file>` | option | Read NUL-separated file list | Safe batching in scripts          |
| `--help`               | flag   | Show help                    | Quick reference                   |
| `--version`            | flag   | Show version                 | Environment validation            |



























