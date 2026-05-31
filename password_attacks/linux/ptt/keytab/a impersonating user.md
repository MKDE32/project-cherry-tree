# LIST INFOS
```
klist -k -t /opt/specialfiles/luser.keytab
```
- we can now impersonate the user with kinit
- kinit is case-sensitive



# IMPERSONATEING
```
klist
```
>Default principal: luser@EXAMPLE.COM

```
kinit vollluser@EXAMPLE.COM -k -t /opt/specialfiles/vollluser.keytab
```

```
klist
```
>Default principal: vollluser@EXAMPLE.COM



# ACCESS TO SMB SHARE
```
smbclient //dc01/vollluser -k -c ls
```

