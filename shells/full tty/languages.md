
spawnt tty shell with python
python -c 'import pty; pty.spawn("/bin/sh")'

oder zb mit bash und python 3
python3 -c 'import pty; pty.spawn("/bin/bash")'

spawnt tty shell with bourne shell
/bin/sh -i

spawnt tty shell with perl
perl —e 'exec "/bin/sh";'

spawnt tty shell with ruby
ruby: exec "/bin/sh"

spawnt tty shell with
lua: os.execute('/bin/sh')

mit awk
awk 'BEGIN {system("/bin/sh")}'

mit find
find / -name nameoffile -exec /bin/awk 'BEGIN {system("/bin/sh")}' \;

mit exec
find . -exec /bin/sh \; -quit

mit vim
vim -c ':!/bin/sh'

vim escape
vim
:set shell=/bin/sh
:shell
