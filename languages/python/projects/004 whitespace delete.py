#entfernt leere Zeilen

input_file = "liste.txt"
output_file = "output.txt"

with open(input_file, "r", encoding="utf-8") as infile, \
open(output_file, "w", encoding="utf-8") as outfile:

    for line in infile:
        if line.strip():
            outfile.write(line)

print(f"Leere Zeilen entfernt. Ergebnis in {output_file} gespeichert")




