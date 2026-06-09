deletes all after and inclusive the first :

```
# Name der Eingabedatei
input_file = "datei.txt"
# Name der Ausgabedatei
output_file = "ausgabe.txt"

# Datei Zeile für Zeile bearbeiten
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        # Alles ab dem Doppelpunkt entfernen
        outfile.write(line.split(":")[0] + "\n")

print(f"Bearbeitung abgeschlossen. Ergebnis in {output_file} gespeichert.")
```
