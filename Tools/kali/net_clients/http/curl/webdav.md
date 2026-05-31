auf webdav mit curl testen
```
root@kali# echo 0xdf > test.txt
root@kali# curl -X PUT http://10.10.10.15/df.txt -d @test.txt 
root@kali# curl http://10.10.10.15/df.txt
0xdf
```
