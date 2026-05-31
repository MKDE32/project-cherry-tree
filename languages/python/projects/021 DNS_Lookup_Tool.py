#pip install dnspython



import dns.resolver



def lookup(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [r.to_text() for r in answers]
    except Exception as e:
        return [f"Fehler {e}"]

if __name__ == "__main__":
    domain = input("Domain: ")
    record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]

    for rtype in record_types:
        print(f"\n{rtype} Records:")
        results = lookup(domain, rtype)
        for r in results:
            print(" -", r)












