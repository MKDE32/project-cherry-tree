| Filter               | Meaning               |
| -------------------- | --------------------- |
| `host 10.10.10.5`    | Traffic to/from host  |
| `src host IP`        | Source host only      |
| `dst host IP`        | Destination host only |
| `port 80`            | Specific port         |
| `portrange 1-1024`   | Port range            |
| `tcp`                | TCP traffic           |
| `udp`                | UDP traffic           |
| `icmp`               | ICMP traffic          |
| `net 192.168.1.0/24` | Entire subnet         |
| `not port 22`        | Exclude SSH           |
