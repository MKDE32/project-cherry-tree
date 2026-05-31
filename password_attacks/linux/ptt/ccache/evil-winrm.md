# using evil winrm with kerberos
```
sudo apt-get install krb5-user -y
cat /etc/krb5.conf
```


>[libdefaults]
>        default_realm = EX.COM  
>  
>...SNIP...  
>  
>[realms]  
>    EX.COM = {  
>        kdc = dc01.ex.com  
>    }  
>  
>...SNIP...

```
proxychains evil-winrm -i dc01 -r inlanefreight.htb
```
