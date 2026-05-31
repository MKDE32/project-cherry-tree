# LOCKSCREEN DISABLE (not tried)
## SHELL OPEN
```
adb shell
```

## SUPERUSER
```
su
```

## PATH
```
cd /data/system
```

## LIST DIRECTORY
```
ls
```

## OPEN LOCKSETTINGS:DB
```
sqlite3
.open locksettings.db
```

## SHOW SQLITE COMMANDS
```
.help
```

## SHOW DB
```
.tables
```

## SELECT ALL FROM DBNAME
```
select * from locksettings;
```

## UPDATE DB
```
UPDATE locksettings SET value = '1' WHERE name = 'lockscreen.disabled';
UPDATE locksettings SET value = '0' WHERE name = 'lockscreen.password_type';
UPDATE locksettings SET value = '0' WHERE name = 'lockscreen.password_type_alternate';
```

## CHECK ENTRIES
```
select * from locksettings;
```

## LEAVE SQLITE3
```
.quit
```

## LEAVE SHELL
```
exit
```

## RESTART ANDROID
dont forget!
