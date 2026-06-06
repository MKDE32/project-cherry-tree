# useful

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


# cred hunting

| Purpose | Filter |
|----------|--------|
| HTTP Basic Auth | `http.authorization` |
| FTP Credentials | `ftp.request.command == "USER" \|\| ftp.request.command == "PASS"` |
| NTLM Authentication | `ntlmssp` |
| Kerberos Authentication | `kerberos` |
| LDAP Bind Requests | `ldap` |



















