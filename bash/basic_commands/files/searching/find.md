beispiel
sudo find / -type f -name "Responder.conf" 2>/dev/null

datei/Ordner suchen (langsam)
find location options

find current directory
find . options

find zusammen mit grep
find . -type f -exec

optionen:
-type f					nur files
-type d					nur directorys
iname “bla.txt”		no case sensetivity
-perm 0664			nur permission 0664		
-size +400k			nur größer als 400k
-not						nicht
-maxdepth 1			bestimmt die Tiefe desdirectorys
-exec blabla +		führt alles bis zum + Zeichen aus
