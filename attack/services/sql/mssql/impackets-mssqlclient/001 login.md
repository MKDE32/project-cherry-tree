
# normal auth
```
impacket-mssqlclient 'mssqlsvc:princess1@10.129.96.31'
```



# windows auth
```
impacket-mssqlclient 'mssqlsvc:princess1@10.129.96.31' -windows-auth
impacket-mssqlclient -windows-auth 'WIN-HARD/luser:supersecurepass@10.129.203.10'
```
