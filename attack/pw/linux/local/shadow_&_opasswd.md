# ETC/SHADOW
```
user      :  $ y   $ j9T   $ 3QS.gHC : 18955         : 0         : 99999     :         7        :                   :                 :
username  :  $ id  $ salt  $ pwhash  :  last change  :  min age  :  max age  :  warning period  : inactivity period : expiration date : reserved field
```
# ETC/SHADOW ID
```
1	      MD5
2a	    Blowfish
5	      SHA-256
6	      SHA-512
sha1	  SHA1crypt
y	      Yescrypt
gy	    Gost-yescrypt
7	      Scrypt
```


# ETC/SECURITY/OPASSWD
```
sudo cat /etc/security/opasswd
```
CONTAINS OLD PASSWORD HASHES



# UNSHADOW
```
sudo cp /etc/passwd /tmp/passwd.bak 
sudo cp /etc/shadow /tmp/shadow.bak 
unshadow /tmp/passwd.bak /tmp/shadow.bak > /tmp/unshadowed.hashes
```



# JOHN SINGLE CRACK MODE OR HASHCAT
```
john --single /tmp/unshadowed.hashes
hashcat -m 1800 -a 0 /tmp/unshadowed.hashes rockyou.txt -o /tmp/unshadowed.cracked
```















