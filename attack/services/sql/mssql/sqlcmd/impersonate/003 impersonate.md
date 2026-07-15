# impersonate user
```
EXECUTE AS LOGIN = 'anotherluser'
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
GO
```

If a user you are trying to impersonate doesn't have access to the DB you are connected with, try to move to the master DB using USE master.





