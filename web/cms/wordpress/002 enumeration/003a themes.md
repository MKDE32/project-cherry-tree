# reminder
not all themes can be detected passive!

# passive enum
```
curl -s -X GET http://blog.inlanefreight.com | sed 's/href=/\n/g' | sed 's/src=/\n/g' | grep 'themes' | cut -d"'" -f2
```

# active enum
same technique as with the plugins



