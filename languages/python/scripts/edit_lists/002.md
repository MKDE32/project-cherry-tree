löscht doppelte zeilen
```
# Name der Eingabedatei
input_file = "ausgabe.txt"
# Name der Ausgabedatei
output_file = "ausgabe2.txt"

# Doppelte Zeilen entfernen
with open(input_file, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

# Nur eindeutige Zeilen behalten, Reihenfolge beibehalten
unique_lines = list(dict.fromkeys(lines))

# Ergebnis speichern
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.writelines(unique_lines)

print(f"Doppelte Einträge entfernt. Ergebnis in {output_file} gespeichert.")
```
