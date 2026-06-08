# reminder
- not all plugins can be detected passive!
- even a deactivated plugin can be a security risk!

# passive enum
```
curl -s -X GET http://blog.inlanefreight.com | sed 's/href=/\n/g' | sed 's/src=/\n/g' | grep 'wp-content/plugins/*' | cut -d"'" -f2
```

# active enum
```
curl -I -X GET http://blog.inlanefreight.com/wp-content/plugins/mail-masta
```
- if the plugin exist we get acess or redirect
- if not we get a 404 not found
