import re

with open("input.txt", "r", encoding="utf-8") as infile, \
     open("output.txt", "w", encoding="utf-8") as outfile:

    for line in infile:
        match = re.search(r"'(https?://[^']+)'", line)
        if match:
            outfile.write(match.group(1) + "\n")
