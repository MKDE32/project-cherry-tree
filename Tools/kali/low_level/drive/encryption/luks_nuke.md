Überblick verschaffen
lsblk -f

richtiges device auswählen (welches schon verschlüsselt ist)
mit slot0 ist die passphrase befüllt (slot 0 enabled
cryptsetup luksDump /dev/sda5


verschlüsslungspassphrase eingeben anschließend selbstzerstörungspassphrase eingeben
cryptsetup luksAddNuke /dev/sda5
sudo dpkg-reconfigure cryptsetup-nuke-password


in slot1 ist nun die passphrase zur selbstzerstörung enthalten (slot 1 enabled)
cryptsetup luksDump /dev/sda5











es ist möglich den header zu sichern und so die selbstzerstörung rückgängig zu machen
file sichern mit dem befehlen:
cryptsetup luksHeaderBackup --header-backup-file luksheader.back /dev/sda5
file luksheader.back



ggf kann der header noch verschlüsselt werden
openssl enc -aes-256-cbc -salt -in luksheader.back -out luksheader.back.enc



wieder entschlüsseln mit
openssl enc -d -aes-256-cbc -in luksheader.back.enc -out luksheader.back



den header wiederherstellen
cryptsetup luksHeaderRestore --header-backup-file luksheader.back /dev/sda5



slot 0 und 1 sollten nun wieder enabled sein
cryptsetup luksDump /dev/sda5
