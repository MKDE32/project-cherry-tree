ROOT VERZEICHNIS
/var/www/html

AUTOMATISCHER START
systemctl enable apache2

START
service apache2 start

STATUS
service apache2 status

ACCESS LOG
/var/log/apache2/access.log
