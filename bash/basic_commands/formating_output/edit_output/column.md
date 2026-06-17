# example
```
column -t file.txt
column -t -s ',' data.csv
column -t -s ':' -o ' | ' /etc/passwd
column -c 100 -t file.txt
```


# flags
| Option        | Type              | Purpose                                           | Typical Use                               |      
| ------------- | ----------------- | ------------------------------------------------- | ----------------------------------------- |
| `-t`          | flag              | Creates a table by aligning columns automatically | Format CSV-like or whitespace data        |      
| `-s <sep>`    | flag              | Sets input column separator                       | Parse CSV (`-s ','`) or custom delimiters |      
| `-o <sep>`    | flag              | Sets output column separator                      | Replace spacing with `                    |
| `-n`          | flag              | Ignores empty fields at line ends                 | Clean irregular data                      |      
| `-e <string>` | flag              | Replace empty fields with string                  | Normalize missing values                  |      
| `-x`          | flag              | Fill columns before rows (transpose layout)       | Horizontal → vertical layout control      |      
| `-c <cols>`   | flag              | Wrap output to terminal width                     | Prevent overflow in logs                  |      
| `-J`          | flag (BSD/macOS)  | JSON-style formatting support (limited variants)  | Structured output formatting              |      
| `--table`     | flag (util-linux) | Enhanced table mode                               | Better formatting heuristics              |      
| `--separator` | flag (long form)  | Same as `-s`                                      | Readability in scripts                    |      

















