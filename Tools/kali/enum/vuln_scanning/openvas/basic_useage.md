# OPENVAS INSTALLIEREN
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get install openvas
sudo openvas-setup
```

die setup routine zeigt dann folgendes zum schluss an:
- eine 127.0.0.1:X browseradresse unter der wir openvas öffnen können
- einen usernamen und ein passwort mit dem wir uns dort anmelden können, unbedingt merken!!

# START OPENVAS SERVICES
```
openvas-start
```

öffnen wir die adresse im browser und loggen uns ein ändern wir als erstes das passwort unter administration/users

# IMPORTOPENVASREPORT
```
db import Pfad/XXXXX.xml
```

# TROUBLESHOOTING
```
openvas-check-setup
```
