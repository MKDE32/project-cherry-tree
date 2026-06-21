# autoroute
```
autoroute
```
- select the internal interface of the pivot host
- space to select, enter to confirm
- `create new interface`
- start tunnel with `y`


# adding a hosts file
```
cat << EOF > hosts
172.16.119.13
172.16.119.7
172.16.119.10
172.16.119.11
EOF
```
- in the directory where ligolo is

```
nxc rdp hosts -u hwilliam -p 'dealer-screwed-gym1'
```


