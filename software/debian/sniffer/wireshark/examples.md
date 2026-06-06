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
