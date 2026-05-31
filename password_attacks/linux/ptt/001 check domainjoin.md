# IDENTIFYING AD INTEGRATION
## REALM
```
realm list
```
>`example.com`  
>type: `kerberos`  
>... SNIP ...  
>permitted-logins: `david@example.com`, `julio@example.com`  
>permitted-groups: `Linux Admins`



## ALTERNATIVES
```
ps -ef | grep -i "winbind\|sssd"
```
- alternatives to `realm`: `sssd` or `winbind`



