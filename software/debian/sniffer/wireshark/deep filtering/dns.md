## DNS Analysis

| Purpose | Filter |
|----------|--------|
| All DNS | `dns` |
| DNS Queries | `dns.flags.response == 0` |
| DNS Responses | `dns.flags.response == 1` |
| NXDOMAIN Responses | `dns.flags.rcode == 3` |
| Specific Domain | `dns.qry.name contains "example.com"` |



