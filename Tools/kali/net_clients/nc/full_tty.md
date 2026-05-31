# UPGRADE TO FULL TTY SHELL
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
```
```
script /dev/null -c bash
```
```
export TERM=xterm
```

`Control + z`

```
stty raw -echo && fg
```

press `return` twice
