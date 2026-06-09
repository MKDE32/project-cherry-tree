clearer presentation of tcpdump
```
import re

pattern = re.compile(
    r'(?P<time>\d+:\d+:\d+\.\d+)\s+IP\s+'
    r'(?P<src_ip>\d+\.\d+\.\d+\.\d+)\.(?P<src_port>\d+)'
    r'\s+>\s+'
    r'(?P<dst_ip>\d+\.\d+\.\d+\.\d+)\.(?P<dst_port>\d+):\s+'
    r'Flags\s+\[(?P<flags>[^\]]+)\]'
)

seq_pattern = re.compile(r'seq\s+([0-9:]+)')
ack_pattern = re.compile(r'ack\s+([0-9]+)')

def fmt(x, width):
    return str(x)[:width].ljust(width)

print(
    f"{'TIME':<15} {'SOURCE':<22} {'DEST':<22} "
    f"{'FLAGS':<8} {'SEQ':<12} {'ACK':<10}"
)
print("-" * 95)

with open("tcpdump.txt", "r", encoding="utf-8") as f:
    for line in f:
        m = pattern.search(line)
        if not m:
            continue

        seq = "-"
        ack = "-"

        s = seq_pattern.search(line)
        a = ack_pattern.search(line)

        if s:
            seq = s.group(1)
        if a:
            ack = a.group(1)

        src = f"{m['src_ip']}:{m['src_port']}"
        dst = f"{m['dst_ip']}:{m['dst_port']}"

        print(
            f"{fmt(m['time'],15)} "
            f"{fmt(src,22)} "
            f"{fmt(dst,22)} "
            f"{fmt(m['flags'],8)} "
            f"{fmt(seq,12)} "
            f"{fmt(ack,10)}"
        )
```
