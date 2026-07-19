# smtp commands
## VRFY
```
telnet 10.10.110.20 25
VRFY root
```
>252 2.0.0 root

```
VRFY luser
```
>550 5.1.1 <luser>: Recipient address rejected: User unknown in local recipient table





## EXPN
```
telnet 10.10.110.20 25
EXPN support-team
```
>250 2.0.0 luser@google.com  
250 2.1.5 lluser@google.com




## RCPT TO























