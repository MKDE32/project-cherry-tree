START / STOP
start daemon
systemctl start cron

stops a daemon
systemctl stop cron

restart daemon
systemctl restart cron



AUTOSTART / STOP
automatisch starten
systemctl enable dienst

nicht automatisch starten
systemctl disable dienst



STATUS
status daemon
systemctl status cron

listet systemctl units auf die aktiv und im memory sind
systemctl list-units

listet systemctl units auf die im memory sind
systemctl list-units --all

listet systemctl units auf die nicht im memory sind
systemctl list-units-files






drucker “hello” broadcast abschalten
systemctl disable cups-browsed
The primary function of cups-browsed  is to enable the automatic discovery of remote queues and their display  in printing dialogues of applications and with command-line tools
This should prevent Fingerprinting

disables the avahi daemon
systemctl disable avahi-daemon
disables the daemon that can run communication with apple protocols
