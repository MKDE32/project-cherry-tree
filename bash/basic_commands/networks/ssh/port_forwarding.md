multiple ports forwarding
ssh -L 1234:localhost:3306 -L 8080:localhost:80 ubuntu@10.129.202.64
forwards 1234 to localhost:3306 and 8080 to localhost:80
local port:server:port


Enabling Dynamic Port Forwarding with SSH
ssh -D 9050 ubuntu@10.129.202.64
localpor=9050 Zielserver 10.129.202.64

Reverse Port Forwarding
ssh -R 80:localhost:80 localhost.run
Verbindungen, die auf Port 80 des Servers localhost.run eingehen, werden zu Port 80 auf deinem lokalen Rechner weitergeleitet.
