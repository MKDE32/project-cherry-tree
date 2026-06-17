```
showmount -e 192.168.1.10
```


mount host:/path/to/export /local/mount/point

• showmount -e host: Dieser Befehl zeigt alle exportierten Verzeichnisse des angegebenen Hosts an.
• showmount -a host: Dieser Befehl zeigt alle Clients an, die auf das angegebene Verzeichnis zugreifen dürfen.
• showmount --exports host: Dieser Befehl zeigt alle exportierten Verzeichnisse und die Clients, die darauf zugreifen dürfen, des angegebenen Hosts an.













Show Available NFS Shares
showmount -e 10.129.14.128

Mounting NFS Share
mkdir target-NFS
mount -t nfs 10.129.14.128:/ ./target-NFS/ -o nolock
