
```
curl -X POST -d "<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>admin</value></param><param><value>CORRECT-PASSWORD</value></param></params></methodCall>" http://blog.inlanefreight.com/xmlrpc.php
```
right password example:  

><?xml version="1.0" encoding="UTF-8"?>  
<methodResponse>  
...  
<member><name>isAdmin</name><value><boolean>1</boolean></value></member>  
<member><name>url</name><value><string>http://blog.inlanefreight.com/</string></value></member>  
>  <member><name>blogid</name><value><string>1</string></value></member>  
>  <member><name>blogName</name><value><string>Inlanefreight</string></value></member>  
>  <member><name>xmlrpc</name><value><string>http://blog.inlanefreight.com/xmlrpc.php</string></value></member>  
> ...  








































