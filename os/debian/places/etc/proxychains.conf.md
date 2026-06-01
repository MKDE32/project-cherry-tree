# example config
>dynamic_chain  
proxy_dns  
tcp_connect_time_out 8000  
tcp_read_time_out 15000  
>
>[ProxyList]  
socks5 127.0.0.1 9050

# options
| Option                 | Example                         | Purpose                                                                       | Typical Use                                    |
| ---------------------- | ------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------- |
| `strict_chain`         | `strict_chain`                  | Uses proxies in the exact listed order. If one proxy fails, connection fails. | Multi-hop anonymity where route order matters. |
| `dynamic_chain`        | `dynamic_chain`                 | Skips dead proxies and uses working ones dynamically.                         | Most practical default for reliability.        |
| `random_chain`         | `random_chain`                  | Randomly selects proxies from the list.                                       | Basic traffic randomization.                   |
| `round_robin_chain`    | `round_robin_chain`             | Rotates proxies sequentially.                                                 | Load distribution/testing.                     |
| `chain_len`            | `chain_len = 2`                 | Number of proxies used with `random_chain`.                                   | Control hop count.                             |
| `proxy_dns`            | `proxy_dns`                     | Sends DNS queries through the proxy chain.                                    | Prevent DNS leaks.                             |
| `remote_dns_subnet`    | `remote_dns_subnet 224`         | Internal subnet used for proxied DNS mapping.                                 | Usually left default.                          |
| `tcp_read_time_out`    | `tcp_read_time_out 15000`       | Read timeout in milliseconds.                                                 | Slow/unreliable proxies.                       |
| `tcp_connect_time_out` | `tcp_connect_time_out 8000`     | Connection timeout in milliseconds.                                           | Faster failure handling.                       |
| `localnet`             | `localnet 127.0.0.0/255.0.0.0`  | Excludes local addresses from proxying.                                       | Avoid proxying LAN/local traffic.              |
| `quiet_mode`           | `quiet_mode`                    | Suppresses runtime messages.                                                  | Cleaner scripting/automation.                  |
| `[ProxyList]`          | `[ProxyList]`                   | Section containing proxy entries.                                             | Required configuration block.                  |
| `socks4`               | `socks4 127.0.0.1 9050`         | SOCKS4 proxy definition.                                                      | Legacy SOCKS support.                          |
| `socks5`               | `socks5 127.0.0.1 9050`         | SOCKS5 proxy definition.                                                      | Most common with Tor.                          |
| `http`                 | `http 192.168.1.10 8080`        | HTTP CONNECT proxy.                                                           | Corporate/web proxies.                         |
| Proxy auth             | `socks5 1.2.3.4 1080 user pass` | Username/password authentication.                                             | Authenticated proxies.                         |

| Situation            | Recommended Setting           |
| -------------------- | ----------------------------- |
| Using Tor            | `dynamic_chain` + `proxy_dns` |
| Avoid DNS leaks      | `proxy_dns`                   |
| Multi-hop anonymity  | `strict_chain`                |
| Testing many proxies | `random_chain`                |
| Automation/scripts   | `quiet_mode`                  |
| Slow proxies         | Increase timeout values       |


| Distribution   | Config Path                       |
| -------------- | --------------------------------- |
| System-wide    | `/etc/proxychains.conf`           |
| ProxyChains-NG | `/etc/proxychains4.conf`          |
| User-specific  | `~/.proxychains/proxychains.conf` |










