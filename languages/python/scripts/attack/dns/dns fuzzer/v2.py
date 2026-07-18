import asyncio
import aiodns


DOMAIN = "inlanefreight.htb"
WORDLIST = "./namelist.txt"
DNS_SERVER = "10.129.203.6"

CONCURRENT = 50


async def check_subdomain(resolver, sub):
    host = f"{sub}.{DOMAIN}"

    try:
        result = await resolver.query(host, "A")

        ips = [r.host for r in result]

        print(f"[+] {host} -> {', '.join(ips)}")

    except aiodns.error.DNSError as e:
        # NXDOMAIN = Subdomain existiert nicht -> ignorieren
        if e.args[0] == 4:
            pass

        # REFUSED anzeigen
        elif e.args[0] == 5:
            print(f"[!] {host} -> REFUSED")

        else:
            print(f"[!] {host} -> DNS Error: {e}")

    except Exception as e:
        print(f"[!] {host} -> Error: {e}")


async def worker(queue, resolver):
    while True:
        sub = await queue.get()

        try:
            await check_subdomain(resolver, sub)

        finally:
            queue.task_done()


async def main():

    resolver = aiodns.DNSResolver(
        nameservers=[DNS_SERVER],
        timeout=3,
        tries=1
    )

    queue = asyncio.Queue()

    with open(WORDLIST) as f:
        for line in f:
            sub = line.strip()

            if sub:
                queue.put_nowait(sub)


    workers = [
        asyncio.create_task(worker(queue, resolver))
        for _ in range(CONCURRENT)
    ]

    await queue.join()

    for w in workers:
        w.cancel()


if __name__ == "__main__":
    asyncio.run(main())
