# TRANSFER TO PIVOT HOST
```
scp chisel ubuntu@10.129.202.64:~/
```
# RUNNING ON PIVOT HOST
```
./chisel server -v -p 1234 --socks5
```
# CONNECTING TO PIVOT HOST
```
./chisel client -v 10.129.202.64:1234 socks
```

# MODIFYING /etc/proxychains.conf
```
socks5 127.0.0.1 1080
```

# USING RDP
```
proxychains xfreerdp /v:172.16.5.19 /u:victor /p:pass@123
```





