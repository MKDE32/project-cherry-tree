```
python3 -c 'import pty; pty.spawn("/bin/bash")'

CTRL + Z
stty raw -echo
fg

reset
export TERM=xterm

stty rows 40 columns 120
```





