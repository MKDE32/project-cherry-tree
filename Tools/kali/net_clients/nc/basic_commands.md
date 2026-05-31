# EXAMPLE
## LISTEN
```
nc -lvnp 1234
```

## BANNER GRABBING
```
nc -nv ip port
```
grab banner

## RANGE SCANNING
```
nc -v -w 5 192.168.178.25 1-443
```
gibt alle offenen ports und ihre services aus





# FLAGS
|       |     |
|------|--------|
| -l | listen mode |
| -v | verbose mode |
| -n | disable dns resolution and only connect from/to ips |
| -p 1234 | set port |
| -w | sets timeouts |



