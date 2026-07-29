```
enum4linux -U 172.16.14.5  | grep "user:" | cut -f2 -d"[" | cut -f1 -d"]"
````
