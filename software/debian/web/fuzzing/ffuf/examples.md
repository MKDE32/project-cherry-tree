# directory fuzzing
```
ffuf -w /Path/wordlist.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ -ic
```

# file fuzzing
```
ffuf -w ./med.txt:FUZZ -u http://154.57.164.83:30798/webfuzzing_hidden_path/flag/FUZZ -ic -e .php,.html,.txt -v
```


## EXTENSION FUZZING
ffuf -w /Path/wordlist.txt:FUZZ -u http://SERVER_IP:PORT/indexFUZZ -ic

## PAGE FUZZING
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://SERVER_IP:PORT/blog/FUZZ.php

## RECURSIVE FUZZING
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -e .php -v

## SUBDOMAIN FUZZING
ffuf -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u https://FUZZ.google.com/

## VHOST SUBDOMAIN FUZZING
ffuf -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://IP_ADDRESSE:PORT/ -H 'Host: FUZZ.google.com'

## PARAMETER FUZZING GET
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://admin.google.com:PORT/admin/admin.php?FUZZ=key -fs xxx

## PARAMETER FUZZING POST
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://admin.google.com:PORT/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx

## VALUE FUZZING POST
ffuf -w ids.txt:FUZZ -u http://admin.google.com:PORT/admin/admin.php -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx

## TRY ID
curl http://admin.google.com:PORT/admin/admin.php -X POST -d 'id=key' -H 'Content-Type: application/x-www-form-urlencoded'

## FOLDER+WORDLIST+EXTENSION FUZZING
ffuf -w ./folders.txt:FOLDERS,./wordlist.txt:WORDLIST,./extensions.txt:EXTENSIONS -u http://192.168.10.10/FOLDERS/WORDLISTEXTENSIONS



























