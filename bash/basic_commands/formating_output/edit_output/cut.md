# EXAMPLE
```
cat dateiname | cut -d" " -f2
```

# FLAGS
`-c 9-14`
- gibt für jede zeile die zeichen 9-14 aus

`-c 9-`
- gibt für jede zeile alles ab zeichen 9 aus

`-d":"`
- beschreibt dabei das Zeichen, das die Felder trennt. hier doppelpunkt.  

`-d" " -f2`
- zweite spalte soll ausgegeben werden

`cut -d" " -f1,7`
- erste und siebte spalte soll ausgegeben werden  







# INFO
Probleme gibt es bei sonderzeichen wegen fehlender utf-8 unterstützung















