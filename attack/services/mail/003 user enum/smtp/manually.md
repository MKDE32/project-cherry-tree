# smtp commands
## VRFY
```
telnet 10.10.110.21 25
HELO x
VRFY root
```
>252 2.0.0 root

```
VRFY luser
```
>550 5.1.1 <luser>: Recipient address rejected: User unknown in local recipient table





## EXPN
```
telnet 10.10.110.21 25
HELO x
EXPN support-team
```
>250 2.0.0 luser@google.com  
250 2.1.5 lluser@google.com




## RCPT TO
```
telnet 10.10.110.21 25
HELO x
MAIL FROM:test@google.com
RCPT TO:luser
```
>250 2.1.0 test@google.com... Sender ok

```
RCPT TO:luser
```
>550 5.1.1 luser... User unknown

```
RCPT TO:lluser
```
>250 2.1.5 lluser... Recipient ok













