```
ldapsearch -h 172.16.8.5 -x -b "DC=GOOGLE,DC=LOCAL" -s sub "*" | grep -m 1 -B 10 pwdHistoryLength
```
