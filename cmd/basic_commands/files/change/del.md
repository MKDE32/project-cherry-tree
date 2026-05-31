
löscht die Datei Bild.jpg
del Bild.jpg

erzwingt das löschen einer versteckten Datei
del /A:H /F datei.dateiendung


/P            Fordert Sie vor dem Löschen jeder Datei zur Bestätigung auf.
/F            Erzwingt das Löschen schreibgeschützter Dateien.
/S            Löscht alle Dateien in allen Unterverzeichnissen.
/Q            Keine Rückfrage bei Verwendung globaler Platzhalter.
/A            Wählt die zu löschenden Dateien nach dem Attribut aus.
Attribute     R  Schreibgeschützte Dateien     S  Systemdateien
                H  Versteckte Dateien            A  Zu archivierende Dateien
                I  Nicht indizierte Dateien      L  Analysepunkte
                O  Offlinedateien
                -  vorangestellt kehrt die Bedeutung um.
