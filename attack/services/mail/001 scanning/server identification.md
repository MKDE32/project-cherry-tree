# mx records


# mx records
```
host -t MX microsoft.com
```
>microsoft.com mail is handled by 10 microsoft-com.mail.protection.outlook.com.

```
dig mx google.com | grep "MX" | grep -v ";"
```
>google.com.      300     IN      MX      10 mail1.google.com.



# a records
```
host -t A mail1.google.com.
```
>mail1.google.com has address 10.129.3.9


# nmap scan
```
sudo nmap -Pn -sV -sC -p25,143,110,465,587,993,995 10.129.3.9
```

























