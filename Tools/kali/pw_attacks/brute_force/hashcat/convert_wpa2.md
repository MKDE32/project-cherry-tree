Upload and convert a WPA / WPA2 pcap capture file to a hashcat capture file
https://hashcat.net/cap2hccapx/
dann bruteforcen mit:
hashcat -m 2500 /.hccat /rockyou.txt



ODER OFFLINE WIE FOLGT:



cleanup des .cap files
wpaclean /small.cap /big.cap

convert small.cap to hccat format
aircrack-ng /small.cap -J namederneuen datei

bruteforcen mit hashcat
hashcat -m 2500 /.hccat /rockyou.txt
