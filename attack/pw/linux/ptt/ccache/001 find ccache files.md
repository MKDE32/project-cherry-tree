# SEARCHING IN ENV VARS
```
env | grep -i krb5
```
>KRB5CCNAME=FILE:/tmp/krb5cc_647412606_qd2Pfh


# SEARCHING IN /TEMP
```
ls -la /tmp
```
>-rw-------  1 luser@test.de  domain users@example.com 1406 Oct  6 16:38 krb5cc_647405106_tBswau  
>-rw-------  1 vollluser@example.com  domain users@example.com 1406 Oct  6 15:23 krb5cc_647481107_Gf415d

# DETERMINE THE NEXT TARGET
```
id luser@test.de
```
>groups=.........domain admins@test.de........

- luser is in the group of domain admins!


















