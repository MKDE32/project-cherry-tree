cURL Basic Auth login

curl http://admin:password@inlanefreight.com/ -vvv



GET request

curl http://localhost



cURL GET request with parameter

curl -u admin:password 'http://inlanefreight.com/search.php?port_code=us'



File upload with cURL

curl -X PUT -d @test.txt http://inlanefreight.com/test.txt -vv



Grabbing Web Server Headers

curl -IL https://www.inlanefreight.com



shows headers

curl -I -X GET https://www.inlanefreight.com
