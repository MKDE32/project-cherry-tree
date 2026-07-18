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

    except Exception:
        pass


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
            queue.put_nowait(line.strip())


    workers = [
        asyncio.create_task(worker(queue, resolver))
        for _ in range(CONCURRENT)
    ]

    await queue.join()

    for w in workers:
        w.cancel()


asyncio.run(main())
