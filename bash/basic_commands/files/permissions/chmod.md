CHMOD ANZEIGEN
ls -l




ausführbar machen
chmod +x file.fileendung

CHANGE USER PERMISSION
chmod u+x file.txt

CHANGE GROUP PERMISSION
chmod g-r file.txt

CHANGE ALL SUB DIRECTORIES RECURSIVELY
chmod -r g-r test




ALL PERMISSIONS TO ALL ROLES
chmod 777 file

Besitzer der Datei     u     1. Ziffer
Gruppe der Datei     g     2. Ziffer
Andere Benutzer     	o     3. Ziffer 

0     Keine
1     x					execute
2     w					write
3     w+x				write, execute
4     r					read
5     r+x				read, execute
6     r+w				read, write
7     r+w+x			read, write, execute
