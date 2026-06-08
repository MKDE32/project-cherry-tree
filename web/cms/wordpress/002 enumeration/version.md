# version enum
## html
```
curl -s -X GET http://blog.inlanefreight.com | grep '<meta name="generator"'
```
> ... content="WordPress 5.5.3" ...

## css
>... bootstrap.css?ver=5.5.3' ...


## js
>... validationEngine.js?ver=5.3.3' ...

# plugin enum
```
curl -s -X GET http://blog.inlanefreight.com | sed 's/href=/\n/g' | sed 's/src=/\n/g' | grep 'wp-content/plugins/*' | cut -d"'" -f2
```
# themes enum
```
curl -s -X GET http://blog.inlanefreight.com | sed 's/href=/\n/g' | sed 's/src=/\n/g' | grep 'themes' | cut -d"'" -f2
```




















