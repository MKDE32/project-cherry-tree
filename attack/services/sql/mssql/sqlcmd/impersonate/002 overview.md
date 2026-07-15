- sysadmins can impersonate anyone by default

# check if sysadmin
```
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
go
```

# identify we can impersonate as without sysadmin
```mssql
SELECT distinct b.name
FROM sys.server_permissions a
INNER JOIN sys.server_principals b
ON a.grantor_principal_id = b.principal_id
WHERE a.permission_name = 'IMPERSONATE'
GO
```

























