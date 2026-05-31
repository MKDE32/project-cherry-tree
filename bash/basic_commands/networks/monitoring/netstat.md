Shows network status.
netstat

WATCH OPEN PORTS
netstat -ano

WATCH ACTIVE INTERNET CONNECTIONS
netstat -antp

watch services that are open
netstat -ntpul

watch for port forwarding
netstat -antp | grep 1234
