Wireguard mit .conf Datei verbinden
nmcli connection import type wireguard file wg_config.conf  

BASH Script Wireguard connection ein
#!/bin/bash 
nmcli connection up wg_config  

BASH Script Wireguard connection aus
#!/bin/bash 
nmcli connection down wg_config
