# self building
## install right go version
```
wget https://go.dev/dl/go1.25.4.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.25.4.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc
```



## build static chisel binary
```
git clone https://github.com/jpillora/chisel.git
cd chisel
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o chisel
ldd chisel
```
>not a dynamic executable
- it is necessary to build the same version on attacker and target.
- to do so we need to use a `static clib build`
- to do so we use the `CGO_ENABLED=0` variable
