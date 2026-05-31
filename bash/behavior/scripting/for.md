Basic for loop

```
for i in /etc/rc.*; do
  echo $i
done
```
-----------------------------------------

C-like for loop
```
for ((i = 0 ; i < 100 ; i++)); do
  echo $i
done
```
-----------------------------------------
```
for i in {1..5}; do
    echo "Welcome $i"
done
```
