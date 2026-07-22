# linked server?
```
SELECT srvname, isremote FROM sysservers
GO
```
- 1 means remote server
- 0 means linked server


# adminrights at another linked server?
```
EXECUTE AS LOGIN = 'luser'
EXECUTE('select @@servername, @@version, system_user, is_srvrolemember(''sysadmin'')') AT [LOCAL.TEST.LINKED.SRV]
GO
```
can luser connect to the linked server with sysadminrights?



