
# overview
we can use one of this tools:

`https://github.com/projectdiscovery/subfinder`  
`https://github.com/aboul3la/Sublist3r`
- standarttools

`https://github.com/TheRook/subbrute`
- pure offline

`https://dnsdumpster.com/`
- website

# enum with subfinder
```
./subfinder -d inlanefreight.com -v
```
# enum with subbrute
```
git clone https://github.com/TheRook/subbrute.git >> /dev/null 2>&1
cd subbrute
echo "ns1.inlanefreight.com" > ./resolvers.txt
./subbrute.py inlanefreight.com -s ./names.txt -r ./resolvers.txt
```




