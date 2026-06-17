# example
```
awk -F: '{print $1}' /etc/passwd
awk -v limit=10 'NR <= limit {print $0}' file.txt
awk 'BEGIN {FS=","; OFS=" | "} {print $1, $2}'
```


# flags
| Flag / Option  | Type              | Purpose                          | Typical Use                     |
| -------------- | ----------------- | -------------------------------- | ------------------------------- |
| `-F <fs>`      | CLI option        | Sets input field separator (FS)  | Parse CSV, logs, `-F ','`       |
| `-v var=value` | CLI option        | Passes variable into AWK program | Dynamic parameters (`-v id=10`) |
| `-f file.awk`  | CLI option        | Reads AWK program from file      | Large scripts / reuse           |
| `-W version`   | CLI option (gawk) | Prints AWK version               | Debug environment               |
| `-W help`      | CLI option (gawk) | Lists gawk options               | Discovery                       |
| `$0`           | Built-in          | Entire current record            | Full line processing            |
| `$1,$2,...`    | Built-in          | Field references                 | Column-based parsing            |
| `FS`           | Variable          | Input field separator            | Same as `-F`                    |
| `OFS`          | Variable          | Output field separator           | Formatting output               |
| `RS`           | Variable          | Record separator                 | Multi-line records              |
| `ORS`          | Variable          | Output record separator          | Control newline output          |
| `NR`           | Variable          | Current record number            | Line counting                   |
| `NF`           | Variable          | Number of fields in record       | Field validation                |
| `FILENAME`     | Variable          | Current input file name          | Multi-file processing           |
| `BEGIN`        | Pattern           | Runs before input processing     | Initialization                  |
| `END`          | Pattern           | Runs after processing            | Summaries / totals              |
