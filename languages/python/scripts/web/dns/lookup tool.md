#pip install dnspython


```python
import dns.resolver
import dns.reversename





def create_resolver(dns_server=None, timeout=3):
    resolver = dns.resolver.Resolver()
    resolver.timeout = timeout
    resolver.lifetime = timeout

    if dns_server:
        resolver.nameservers = [dns_server]

    return resolver





def forward_lookup(domain, record_type, resolver):
    try:
        answers = resolver.resolve(domain, record_type)
        return [r.to_text() for r in answers]
    except Exception as e:
        return [f"Fehler {e}"]





def reverse_lookup(ip, resolver):
    try:
        rev_name = dns.reversename.from_address(ip)
        answers = resolver.resolve(rev_name, "PTR")
        return [r.to_text() for r in answers]
    except Exception as e:
        return[f"Fehler: {e}"]





if __name__ == "__main__":
    domain = input("Domain: ").strip()
    dns_server = input("DNS Server: ").strip() or None

    resolver = create_resolver(dns_server)

    if domain:
        record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]
        for rtype in record_types:
            print(f"\n{rtype} Records:")
            for r in forward_lookup(domain, rtype, resolver):
                print(" -", r)
    else:
        ip = input("IP Adresse: ").strip()
        print("\nPTR Records:")
        for r in reverse_lookup(ip, resolver):
            print(" -", r)

```

