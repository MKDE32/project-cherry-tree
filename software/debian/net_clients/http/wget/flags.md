# most common
| Flag                     | Meaning                      | Typical Use Case                   |
| ------------------------ | ---------------------------- | ---------------------------------- |
| `-O <file>`              | Save output to specific file | Rename downloaded payload          |
| `-o <file>`              | Log output to file           | Keep clean terminal / log activity |
| `-q`                     | Quiet mode                   | Reduce noise in scripts            |
| `-v`                     | Verbose mode                 | Debug requests                     |
| `-nv`                    | Non-verbose                  | Minimal but useful output          |
| `-c`                     | Continue download            | Resume interrupted downloads       |
| `--no-check-certificate` | Ignore SSL errors            | Self-signed certs (common in labs) |

# http
| Flag                       | Meaning                   | Typical Use Case                   |
| -------------------------- | ------------------------- | ---------------------------------- |
| `--method=PUT`             | Use custom HTTP method    | Upload attempts (if allowed)       |
| `--body-data="data"`       | Send POST data            | Interact with forms                |
| `--body-file=<file>`       | Send file as request body | Upload payload                     |
| `--header="Header: value"` | Add custom header         | Host header injection, auth bypass |
| `--user-agent="UA"`        | Set User-Agent            | Bypass filters / mimic browser     |
| `--referer="URL"`          | Set Referer header        | Bypass weak access controls        |



# auth
| Flag                     | Meaning                | Typical Use Case           |
| ------------------------ | ---------------------- | -------------------------- |
| `--user=<user>`          | Username               | Login-protected resources  |
| `--password=<pass>`      | Password               | Combine with `--user`      |
| `--http-user=<user>`     | HTTP auth user         | Basic/Digest auth          |
| `--http-password=<pass>` | HTTP auth password     |                            |
| `--auth-no-challenge`    | Send creds immediately | Some misconfigured servers |


# recursive / crawling
| Flag              | Meaning                     | Typical Use Case      |
| ----------------- | --------------------------- | --------------------- |
| `-r`              | Recursive download          | Mirror a website      |
| `-l <depth>`      | Set recursion depth         | Limit crawl scope     |
| `--no-parent`     | Stay in current directory   | Avoid going up paths  |
| `--reject=<list>` | Skip file types             | Ignore images, etc.   |
| `--accept=<list>` | Only download certain types | Target specific files |
| `-np`             | Same as `--no-parent`       | Common shorthand      |




# stealth
| Flag                | Meaning                | Typical Use Case        |
| ------------------- | ---------------------- | ----------------------- |
| `--limit-rate=200k` | Limit bandwidth        | Avoid detection         |
| `--wait=2`          | Delay between requests | Throttle crawling       |
| `--random-wait`     | Random delay           | Evade basic IDS         |
| `--timeout=10`      | Request timeout        | Faster failure handling |
| `--tries=3`         | Retry attempts         | Stability               |






# proxy
| Flag                     | Meaning                | Typical Use Case       |
| ------------------------ | ---------------------- | ---------------------- |
| `-e use_proxy=yes`       | Enable proxy           | Pivoting               |
| `-e http_proxy=IP:PORT`  | Set HTTP proxy         | Use Burp / proxychains |
| `-e https_proxy=IP:PORT` | HTTPS proxy            | Interception           |
| `--bind-address=<IP>`    | Use specific interface | Multi-homed setups     |











































