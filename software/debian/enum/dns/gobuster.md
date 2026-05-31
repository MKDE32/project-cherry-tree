# EXAMPLES
## Directory/File Enumeration of webserver
```
gobuster dir -u http://10.10.10.121/ -w /usr/share/dirb/wordlists/common.txt
```

## DNS Subdomain Enumeration
```
gobuster dns -d inlanefreight.com -w /usr/share/SecLists/Discovery/DNS/namelist.txt
```

## Vhost Subdomain Enumeration
```
gobuster vhost -w /opt/useful/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u http://thetoppers.htb --append-domain
```
use always `--append-domain`





# FLAGS

## SHOW 403
--status-codes 403

## DONT SHOW 404
--status-codes-blacklist "404"

## THREADS
-t

## APPEND .php, .txt, .html
-x php,txt,html
