
requirements aus einem git clone installieren
```
pip3 install -r requirements.txt
```







Manuelle Installation von pip

 Wer eine neuere Version von pip als die aus den Paketquellen benötigt der deinstalliert zunächst das etwaige Ubuntu-Paket[1] und ruft dann den Link https://bootstrap.pypa.io/get-pip.py im Browser oder mittels wget auf, um das Installationsprogramm herunterzuladen.
Sollte  der Browser die Datei nicht zum Download anbieten, sondern „nur“ im  Browserfenster den Quelltext anzeigen, so öffnet man einfach einen  Texteditor, kopiert den kompletten Quelltext aus dem Browserfenster und  fügt ihn im Editor ein. Danach speichert man die Datei unter dem Namen get-pip.py in einem beliebigen Verzeichnis, z.B. im Homeverzeichnis.
Danach wechselt man in dieses Verzeichnis und ruft zur Installation der Python 3 Version den folgenden Befehl auf[2][3]:

sudo python3 get-pip.py 

Jetzt installiert sich pip ins Verzeichnis /usr/local/bin und ist dann einsatzbereit.






Wohin werden mit pip installierte Python-Module installiert?
 Das Verzeichnis, in das pip das Python-Modul (bzw. dessen Dateien)  installiert, hängt davon ab, wie bzw. mit welchen Optionen man pip  aufruft.
Wird pip mit Root-Rechten ausgeführt, befinden sich die installierten Module im Verzeichnis /usr/local/lib/pythonX.Y/dist-packages/ bzw. einem Unterverzeichnis davon, wobei X.Y die Python-Version ist, für die installiert wurde. Sind im Python-Modul ausführbare Programme enthalten, werden diese nach /usr/local/bin abgelegt.
Wird pip mit der Option --user aufgerufen, befinden sich die installierten Module im Verzeichnis ~/.local/lib/pythonX.Y/site-packages bzw. einem Unterverzeichnis davon, wobei X.Y die Python-Version ist, für die installiert wurde. Sind im Python-Modul ausführbare Programm enthalten, werden diese im Homeverzeichnis des Nutzers unter ~/.local/bin abgelegt.

Hinweis:
~/.local/bin ist wegen eines Bugs eventuell nicht im Suchpfad für ausführbare Programme enthalten, man muss das Verzeichnis in diesem Fall manuell der Umgebungsvariable PATH hinzufügen, indem man es in die Datei ~/.profile  einträgt. Danach sollte man sich als Nutzer einmal ab- und dann wieder  neu anmelden, damit die Änderung greift. Siehe dafür auch Umgebungsvariable/Dateien (Abschnitt „Environment-einzelner-oder-aller-Benutzer“) sowie Umgebungsvariable/typische Anwendungsfälle (Abschnitt „PATH-erweitern“). 


Bei Verwendung von pip in Kombination mit venv befinden sich die Module innerhalb des Modulverzeichnisses des „Virtual Environments“.

Wohin sollte man installieren?
 Es gibt selten Gründe, ein Python-Modul systemweit für alle Nutzer zu  installieren. Module, die vom System benötigt werden, werden  normalerweise systemweit über die Paketverwaltung installiert. Von daher  ist die lokale Installation für die Nutzer oder die Installation in ein  lokales „Virtual Environment“ der zu bevorzugende Weg.
Die lokale  Installation bzw. ein lokales „Virtual Environment“ hat weiterhin den  Vorteil, dass man keine Konflikte bzw. Probleme mit Modulen bekommt, die  systemweit über die Paketverwaltung installiert wurden.

Hinweis:
Für  die selbe Python-Version lassen sich standardmäßig Module nicht  parallel lokal für einen Nutzer und systemweit installieren, es ist nur  eine von beiden Installationen möglich.
Wer verschiedene Versionen des gleichen Moduls braucht muss dann auf ein "Virtual Environment" zurück greifen. 



pip ausführen
 pip ist ein Kommandozeilenprogramm. Die allgemeine Syntax für die Python 3 Version lautet[2]:
pip3 BEFEHL [OPTION(EN)] MODUL(E) 

Das für Python 3.4 und neuer verfügbare Modul von pip lässt sich wie folgt nutzen:
python3 -m pip [OPTION(EN)] BEFEHL MODUL(E) 

Wenn  mittels des Befehls ein Modul systemweit installiert oder deinstalliert  wird, dann muss pip mit Root-Rechten aufgerufen werden[3], bei Verwendung der Option --user oder bei der Verwendung innerhalb eines „Virtual Environments“ reichen normale Benutzerrechte.
Zu  beachten ist auch, dass pip – im Gegensatz zum allgemeinen Verhalten  von Linux und Python – nicht "case-sensitve" arbeitet, d.h. Groß- /  Kleinschreibung wird nicht unterschieden. Der Befehl pip3 install modulname installiert das Modul genau so wie pip3 install ModulName.
Einige Befehle sind:
 

| Befehle von pip |  |
| Befehl | Erklärung |
| install MODUL | Installiert das Modul MODUL. Es können auch mehrere Module angegeben werden, die dann alle installiert werden. |
| uninstall MODUL | Deinstalliert das Modul MODUL. Es können auch mehrere Module angegeben werden, die dann alle deinstalliert werden. |
| list | Zeigt die installierten Python-Module an. |
| show MODUL | Zeigt Informationen zum installierten Modul MODUL an. |

Einige Optionen von pip in Kombination mit dem Befehl install sind:
 

| Optionen von pip in Kombination mit dem Befehl install |  |
| Option | Erklärung |
| -U, --upgrade | Aktualisiert das bzw. die nachfolgend angegebene(n) Modul(e) auf die neuste Version. |
| -r requirments.txt | Installiert alle Module, die in der Datei requirments.txt aufgeführt sind. Pro Zeile muss in der Datei ein Modulname stehen. |
| --user | Installiert das bzw. die nachfolgend angegebene(n) Modul(e) lokal für den aktuellen Benutzer. |

Eine Übersicht über die jeweiligen Optionen erhält man über den Aufruf
pip3 BEFEHL -h 

also z.B.:
pip3 install -h 

Eine komplette Übersicht findet man in den Man-Pages von pip.

Beispiele
 Der folgende Befehl installiert das Modul "Markdown" lokal für den aktuellen Benutzer:
pip3 install --user markdown 

 
Collecting markdown
  Downloading Markdown-2.6.11-py2.py3-none-any.whl (78kB)
    100% |████████████████████████████████| 81kB 1.2MB/s 
Installing collected packages: markdown
Successfully installed markdown-2.6.11Die Deinstallation sieht so aus:
pip3 uninstall markdown 

Uninstalling Markdown-2.6.11:
  /home/NUTZER/.local/bin/markdown_py
  /home/NUTZER/.local/lib/python3.5/site-packages/Markdown-2.6.11.dist-info/DESCRIPTION.rst
  ...
  /home/NUTZER/.local/lib/python3.5/site-packages/markdown/extensions/abbr.py
  ...
  /home/NUTZER/.local/lib/python3.5/site-packages/markdown/treeprocessors.py
  /home/NUTZER/.local/lib/python3.5/site-packages/markdown/util.py
Proceed (y/n)? y
  Successfully uninstalled Markdown-2.6.11Mit dem folgenden Befehl wird ein für den aktuellen Benutzer installiertes Modul aktualisiert, hier im Beispiel "Markdown":
pip3 install --user -U markdown 

pip  prüft dabei direkt, ob die Abhängigkeiten des Moduls ebenfalls aktuell  sind. Sonst werden diese auch auf den neusten Stand gebracht. Ist das  Modul systemweit installiert, dann muss die Option --user weg gelassen werden.
Falls  man neben dem Aktualisieren von "Markdown" gleich noch ein weiteres  Modul mit installieren mögen würde, so sähe dies am Beispiel  "streamlink" dann folgendermaßen aus:
pip3 install --user -U markdown streamlink 

Man kann mit pip auch ein Modul gezielt in einer bestimmten Version installieren. Der folgende Befehl würde Django in der Version 1.11.8 installieren:
pip install --user django==1.11.8 

Würde man anschließend pip install -U django  aufrufen, dann würde immer auf die aktuellste Version aktualisiert  (also z.B. 2.0.2) und nicht "nur" auf die nächste Minor-Version (also  z.B. 1.11.9).
Der folgende Befehl zeigt alle installierten Python-Module – auch die, die über die Paketverwaltung von Ubuntu systemweit installiert wurden:
pip3 list 

vergrößern
-lxc (0.1)
apt-xapian-index (0.47)
apturl (0.5.2)
beautifulsoup4 (4.4.1)
...
unity-scope-yelp (0.1)
unity-scope-zotero (0.1)
urllib3 (1.22)
usb-creator (0.3.0)
virtualenv (15.0.1)
wheel (0.29.0)
xdiagnose (3.8.4.1)
xkit (0.0.0)
XlsxWriter (0.7.3)Möchte man nur die für den aktuellen Benutzer lokal installierten Module anzeigen, dann lautet der Befehl
pip3 list --user 

Wie  bereits in der Einleitung erwähnt, kann pip auch Module direkt aus  einem Versionskontrollsystem herunterladen. Im folgenden Beispiel wird  die aktuelle Version von Jinja2: direkt aus dem Git-Repositry lokal installiert:
pip3 install --user https://github.com/pallets/jinja/archive/master.zip 

Details dazu findet man in der offiziellen Dokumentation 🇬🇧.
Wer mehrere Module auf ein Mal installieren möchte, der kann entweder bei install  alle angegeben, zwischen den Modulnamen muss lediglich ein Leerzeichen  stehen. Oder man kann eine einfache Text-Datei anlegen, in den die  Modulnamen aufgeführt sind. Sieht die Datei Namens requirements.txt z.B. so aus:
markdown
jinja2
howdoidann würde der Befehl
pip3 install --user -r requirments.txt 

die Module Markdown, jinja2 und howdoi lokal installieren. Dies würde auch für die Deinstallation mit dem Befehl uninstall funktionieren.

Tipps & Tricks
 

Alle Python-Pakete mit pip auf einmal aktualisieren
 Möchte man mittels pip alle lokalen Python-Pakete aktualisieren, so kann  man sich mit folgender Befehlskette – welche neben pip noch aus grep, cut und xargs besteht – behelfen:
pip3 freeze --user | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip3 install --user -U   


Manuelle Deinstallation
 Hat man die Paketverwaltung pip manuell mit dem Script get-pip.py installiert, kann man diese mit folgendem Befehl wieder deinstallieren.
sudo python3 -m pip uninstall pip 

Da bei der Installation automatisch auch (wenn noch nicht vorhanden) die Python Setuptools installiert werden, kann man den Befehl noch mit setuptools erweitern, falls man die setuptools nicht benötigt:
sudo python3 -m pip uninstall pip setuptools 
