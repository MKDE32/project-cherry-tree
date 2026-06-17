# overview
```
netstat -i
```



# example
```
netstat -tanp
```







| Flag | Meaning | Why it matters in pentesting |
|------|--------|------------------------------|
| -t   | TCP connections | Identify TCP services (SSH, HTTP, DBs) |
| -l   | Listening sockets | Find exposed services on the host |
| -a   | All sockets | Shows both listening and established connections |
| -n   | Numeric output | Faster output, avoids DNS/service resolution |
| -p   | Process info | Maps connections to processes (requires sudo) |
| -r   | Routing table | Understand network paths and gateway routes |
| -i   | Interface stats | Identify active interfaces and traffic patterns |












