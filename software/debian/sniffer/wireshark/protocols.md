## Common Protocols

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

---

## IP Address Filtering

| Purpose | Filter |
|----------|--------|
| Specific Host | `ip.addr == 192.168.1.10` |
| Source IP | `ip.src == 192.168.1.10` |
| Destination IP | `ip.dst == 192.168.1.10` |
| Exclude Host | `!(ip.addr == 192.168.1.10)` |
| IPv6 Traffic | `ipv6` |

---

## Port Filtering

| Purpose | Filter |
|----------|--------|
| Port 80 | `tcp.port == 80` |
| Port 443 | `tcp.port == 443` |
| Source Port | `tcp.srcport == 443` |
| Destination Port | `tcp.dstport == 443` |
| Port Range | `tcp.port >= 1 && tcp.port <= 1024` |

---

## DNS Analysis

| Purpose | Filter |
|----------|--------|
| All DNS | `dns` |
| DNS Queries | `dns.flags.response == 0` |
| DNS Responses | `dns.flags.response == 1` |
| NXDOMAIN Responses | `dns.flags.rcode == 3` |
| Specific Domain | `dns.qry.name contains "example.com"` |

---

## HTTP Analysis

| Purpose | Filter |
|----------|--------|
| HTTP Requests | `http.request` |
| HTTP Responses | `http.response` |
| GET Requests | `http.request.method == "GET"` |
| POST Requests | `http.request.method == "POST"` |
| User-Agent Header | `http.user_agent` |
| HTTP Errors | `http.response.code >= 400` |

---

## TLS / HTTPS Analysis

| Purpose | Filter |
|----------|--------|
| TLS Traffic | `tls` |
| Client Hello | `tls.handshake.type == 1` |
| Server Hello | `tls.handshake.type == 2` |
| SNI Hostname | `tls.handshake.extensions_server_name` |
| Certificate Exchange | `tls.handshake.certificate` |



---

## Network Recon Detection

| Activity | Filter |
|-----------|--------|
| ARP Scan | `arp` |
| ICMP Sweep | `icmp.type == 8` |
| TCP SYN Scan | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |
| SYN/ACK Responses | `tcp.flags.syn == 1 && tcp.flags.ack == 1` |
| RST Responses | `tcp.flags.reset == 1` |

---

## Suspicious Traffic

| Purpose | Filter |
|----------|--------|
| Failed Connections | `tcp.flags.reset == 1` |
| Retransmissions | `tcp.analysis.retransmission` |
| Duplicate ACKs | `tcp.analysis.duplicate_ack` |
| Zero Window | `tcp.window_size == 0` |
| Malformed Packets | `_ws.malformed` |

---

## SMB & Active Directory

| Purpose | Filter |
|----------|--------|
| SMB Traffic | `smb || smb2` |
| Kerberos | `kerberos` |
| LDAP | `ldap` |
| NTLM Authentication | `ntlmssp` |
| DCE/RPC | `dcerpc` |

---

## Useful Searches During Internal Pentests

| Goal | Filter |
|--------|--------|
| Find Cleartext Logins | `http.authorization || ftp.request.command == "PASS"` |
| Discover Internal Hosts | `arp || dns` |
| Spot Port Scans | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |
| Find Domain Controllers | `kerberos || ldap` |
| Identify SMB Servers | `smb || smb2` |
| Detect LLMNR Traffic | `llmnr` |
| Detect NBNS Traffic | `nbns` |
| Detect mDNS Traffic | `mdns` |


