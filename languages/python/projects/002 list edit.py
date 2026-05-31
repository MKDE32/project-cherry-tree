#lösche alles ab dem ersten :

input_file = "liste.txt"
output_file = "output.txt"

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:

    for line in infile:
    	left = line.split(":", 1)[0].strip()
    	if left:
        	outfile.write(left + "\n")

print(f"Bearbeitung abgeschlossen. Ergebnis in {output_file} gespeichert.")












