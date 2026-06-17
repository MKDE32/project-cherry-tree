# examples
## show live
```
watch ss -tp
```

## most common
```
ss -tuln                        # fast service discovery (TCP/UDP listening)
ss -tulnp                       # service discovery + owning process
ss -tanp                        # all TCP connections with processes
ss -tulpn state established     # active connections only
```


# flags
| Flag | Meaning | Why it matters in pentesting |
|------|--------|------------------------------|
| -t   | TCP sockets | Identify TCP services (web, ssh, db, etc.) |
| -l   | Listening sockets | Discover exposed services on the host |
| -a   | All sockets | Shows listening + established connections |
| -n   | Numeric output | Avoid DNS/service name resolution for speed/clarity |
| -p   | Process info | Maps sockets to processes (critical for service ID) |
| -4   | IPv4 only | Focus on common attack surface |



