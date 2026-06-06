# Common Protocols

| Purpose | Display Filter |
|----------|---------------|
| HTTP | `http` |
| HTTPS/TLS | `tls` |
| DNS | `dns` |
| TCP | `tcp` |
| UDP | `udp` |
| ICMP (Ping) | `icmp` |
| ARP | `arp` |
| SMB | `smb || smb2` |
| FTP | `ftp` |
| SSH | `ssh` |
| DHCP | `bootp` |
| LDAP | `ldap` |
| Kerberos | `kerberos` |
| RDP | `tcp.port == 3389` |



# IP Address Filtering

| Purpose | Filter |
|----------|--------|
| Specific Host | `ip.addr == 192.168.1.10` |
| Source IP | `ip.src == 192.168.1.10` |
| Destination IP | `ip.dst == 192.168.1.10` |
| Exclude Host | `!(ip.addr == 192.168.1.10)` |
| IPv6 Traffic | `ipv6` |



# Port Filtering

| Purpose | Filter |
|----------|--------|
| Port 80 | `tcp.port == 80` |
| Port 443 | `tcp.port == 443` |
| Source Port | `tcp.srcport == 443` |
| Destination Port | `tcp.dstport == 443` |
| Port Range | `tcp.port >= 1 && tcp.port <= 1024` |



# Network Recon Detection

| Activity | Filter |
|-----------|--------|
| ARP Scan | `arp` |
| ICMP Sweep | `icmp.type == 8` |
| TCP SYN Scan | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |
| SYN/ACK Responses | `tcp.flags.syn == 1 && tcp.flags.ack == 1` |
| RST Responses | `tcp.flags.reset == 1` |








