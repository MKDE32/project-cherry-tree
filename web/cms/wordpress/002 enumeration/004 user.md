# reminder
- u can get usernames when you hover over the link post author by eg. admin
- the author has usually the id 1




# user confirmation
```
curl -s -I http://blog.inlanefreight.com/?author=1
```
>HTTP/1.1 301 Moved Permanently
...
Location: http://blog.inlanefreight.com/index.php/author/admin/

- not existing user gives 404 not found


