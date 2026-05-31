Ersetzen von Text in einer Datei


Jedes Auftreten von "Anton" wird durch "Berta" ersetzt (aber auch "Antonius" wird zu "Bertaius"). Wird g (global) weggelassen, wird nur das erste Auftreten in einer Zeile ersetzt.
sed s/Anton/Berta/g Textdatei 

Jedes Auftreten von "Anton" wird durch "Berta" ersetzt (aber auch "Antonius" wird zu "Bertaius"). 
aber nur in Zeilen, die "HALLO" enthalten
sed /HALLO/s/Anton/Berta/g hallo

Ersetzt alle "Anton" durch "Berta" und gibt nur die betroffenen Zeilen aus.
sed -n s/Anton/Berta/gp Textdatei 



Entfernen von Zeilen
Zeilen die mit # anfangen, werden entfernt.
sed '/^#/d' Textdatei 

 




Zeilen einfügen
• sed '3iNeue Zeile' Textdatei 

 Vor der dritten Zeile wird "Neue Zeile" eingefügt.

• sed '4aNeue Zeile' Textdatei 

 Hier wird "Neue Zeile" nach der vierten Zeile eingefügt.

• sed '$aNeue Zeile' Textdatei 

 Hier wird "Neue Zeile" nach der letzten Zeile eingefügt.





Reguläre Ausdrücke
sed 's/^E-Mail:.*$/E-Mail-Adresse ist privat/' Textdatei 

 Alle Zeilen, die mit "E-Mail:" anfangen, werden ersetzt.



Bearbeiten von Dateinamen
sed 's!/home/anton/!/home/berta/!' Textdatei 

 Normalerweise wird "/" als Trennzeichen verwendet. Es lässt sich aber  beliebig austauschen, was beim Bearbeiten von Dateinamen nützlich ist.





Direktes Bearbeiten einer Datei
• Bearbeiten von PHP Einstellungen (memory_limit) z.B. php.ini 
sed -i "s/memory_limit = .*M/memory_limit = 2048M/" /etc/php/7.2/apache2/php.ini 

 Hier wird der memory_limit von dem Standard-Wert auf memory_limit = 2048M gesetzt. 

• Bearbeiten von PHP Einstellungen (upload_max_filesize) z.B. php.ini 
sed -i "s/upload_max_filesize =.*/upload_max_filesize = 10240M/" /etc/php/7.2/apache2/php.ini 

 Hier wird der memory_limit von dem Standard-Wert auf upload_max_filesize = 10240M gesetzt. 









substituting text. ersetzt jede 5 durch X

cat f | sed 's/5/X/g'
