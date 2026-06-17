sortiert ausgabe alphabetisch oder numerisch

cat /etc/passwd | sort

# flags

| Option           | Type   | Purpose               | Typical Use                             |
| ---------------- | ------ | --------------------- | --------------------------------------- |
| `-n`             | flag   | Numeric sort          | Proper ordering of numbers (`1, 2, 10`) |
| `-r`             | flag   | Reverse order         | Descending sorting                      |
| `-k <key>`       | option | Sort by key/column    | Column-based sorting                    |
| `-t <sep>`       | option | Field separator       | CSV/TSV sorting                         |
| `-u`             | flag   | Unique output         | Deduplicate after sorting               |
| `-f`             | flag   | Case-insensitive      | Ignore uppercase/lowercase              |
| `-h`             | flag   | Human numeric sort    | `1K, 2M, 500`                           |
| `-V`             | flag   | Version sort          | Natural version ordering (`1.9 < 1.10`) |
| `-b`             | flag   | Ignore leading blanks | Clean alignment issues                  |
| `-M`             | flag   | Month sort            | Jan–Dec ordering                        |
| `-c`             | flag   | Check if sorted       | Validation (no output change)           |
| `-C`             | flag   | Check silently        | Exit code only                          |
| `--parallel=<n>` | option | Parallel sorting      | Performance optimization                |
| `--stable`       | flag   | Stable sort           | Preserve equal-order input              |







