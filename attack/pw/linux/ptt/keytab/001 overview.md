# SEARCH KEYTAB FILES
## SEARCH FOR .KEYTAB FILE
```
find / -name *keytab* -ls 2>/dev/null
```

## SEARCHING FOR SCRIPTS
```
crontab -l
```
>*5/ * * * * /home/carlos@example.com/.scripts/kerberos_script_test.sh
```
cat /home/carlos@example.com/.scripts/kerberos_script_test.sh
```
>#!/bin/bash  
>  
>kinit svc_workstations@EXAMPLE.COM -k -t /home/carlos@example.com/.scripts/svc_workstations.kt  
>smbclient //dc01.example.com/svc_workstations -c 'ls'  -k -no-pass > /home/carlos@example.com/script-test-results.txt  

- kinit request the user's tgt and store this ticket in the cache (ccache file)
- we can use kinit to import a keytab into our session and act as the user.
- the script imports a ticket `svc_workstations.kt` for the user `svc_workstations@EXAMPLE.COM` before connect to a shared folder.











