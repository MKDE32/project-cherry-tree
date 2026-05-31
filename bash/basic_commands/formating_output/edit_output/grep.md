no case sensitivity
blablabla | grep -i blubb

grep: blendet alles andere aus
blablabla | grep -o blubb

grep: suchstring soll NICHT angezeigt werden
blablabla | grep -v blubb

grep: Dateien in unterverzeichnissen auch durchsuchen
blablabla | grep -r blubb

grep: Nur auf Vorkommen in ganzen Wörtern beschränken
blablabla | grep -w blubb

grep: liefert die reine Anzahl zurück, sonst nichts.
blablabla | grep -c blubb

outputs the line number
grep -n

############### EXAMPLE ###############
grep -oP "\/documents.*?.pdf"                  /documents/Invoice_3_06_2020.pdf



############### FLAGS ###############
-o                print only matched text
-P                use Perl-Compatible Regular Expressions







nach systemd filtern

find /etc/ -name *.conf 2>/dev/null | grep systemd
