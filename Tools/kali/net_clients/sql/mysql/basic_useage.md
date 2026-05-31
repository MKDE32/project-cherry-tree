mysql -u root -h docker.hackthebox.eu -P 3306 -p

SHOW DATABASES;

USE database

SHOW TABLES;

DESCRIBE table;

SELECT * FROM table_name;

DROP TABLE table_name;

SELECT * FROM logins ORDER BY password;

SELECT * FROM logins LIMIT 2;

SELECT * FROM logins where username = 'admin';

SELECT * FROM logins WHERE username LIKE 'admin%';
