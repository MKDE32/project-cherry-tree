die Ausgabe des folgenden Befehls, der prüft, ob alle Anschlüsse korrekt erkannt wurden
```
xrandr --query
```
Sobald ein zweiter Monitor angeschlossen wird, kann man ihn mit folgendem Befehl aktivieren:
```
xrandr --auto
```

Falls xandr --auto nicht funktioniert: Dabei wird der DVI-Ausgang automatisch konfiguriert (--output DVI-0 --auto) und rechts
 (--right-of) neben dem internen Bildschirm angeordnet. Befehl Ist für mehrere Bildschirme.
```
xrandr --output DVI-0 --auto --right-of LVDS
```

Auflösung einstellen
```
xrandr -s 1280x800
```
