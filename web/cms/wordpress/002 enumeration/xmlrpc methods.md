# info
- this lists all available xmlrpc functions
- this detects the attack surface


```
curl -X POST -d "<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>" http://154.57.164.61:32322/xmlrpc.php | grep string | wc -l
```

