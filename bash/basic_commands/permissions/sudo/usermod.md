Add User to sudo group
usermod -aG sudo <Username>
-a = append; ohne -a werden alle anderen gruppen gelöscht

lock user account
usermod -L

set expiredate
-e YYYY-MM-DD

change gid
-g

new login
-l

change pw
-p

change shell
-s

change user id
-u

unlock user account
-U

selinux user
-Z
