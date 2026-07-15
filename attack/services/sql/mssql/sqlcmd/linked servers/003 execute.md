# send commands to the linked server
```
EXECUTE('select @@servername, @@version, system_user, is_srvrolemember(''sysadmin'')') AT [10.0.0.12\SQLEXPRESS]
GO
```
- ; for multiple commands
- we need to use single double quotes to escape the single quote

