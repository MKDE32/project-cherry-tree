# mount smb share
```
sudo mkdir /mnt/Finance
sudo mount -t cifs -o username=plaintext,password=Password123,domain=. //192.168.220.129/Finance /mnt/Finance
```
