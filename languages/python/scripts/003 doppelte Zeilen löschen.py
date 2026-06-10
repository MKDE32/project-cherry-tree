#lösche doppelte Zeilen

input_file = "liste.txt"
output_file = "output.txt"

with open(input_file, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

unique_lines = list(dict.fromkeys(lines))

with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.writelines(unique_lines)

print(f"Doppelte Einträge wurden entfernt. Ergebnis in {output_file} gespeichert")





