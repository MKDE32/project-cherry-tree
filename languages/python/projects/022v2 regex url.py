import re

url_pattern = re.compile(r'https?://\S+')

with open("input.txt", "r", encoding="utf-8") as infile, \
     open("output.txt", "w", encoding="utf-8") as outfile:

    for line in infile:
        match = url_pattern.search(line)
        if match:
            outfile.write(match.group() + "\n")
