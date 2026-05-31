# PACKAGES
```
pm list packages
pm list packages -f
pm path com.app.name
pm clear com.app.name
```



# TRIGGERING
```
monkey -p com.app.name -c android.intent.category.LAUNCHER 1
am start -n com.app.name/.MainActivity
am start -a android.intent.action.VIEW -d "http://example.com"
```



# DATA
```
ls /sdcard/
ls /data/data/
```



# LOGS
```
logcat
logcat | grep com.app.name
logcat -d > logs.txt
```


# INFO
```
ps
top
getprop
id
whoami
```


# PERMISSIONS
```
dumpsys package com.app.name
pm list permissions
```


# NETWORK
```
netstat
ip addr
ping 8.8.8.8
```


# TEST CONTENT PROVIDER
```
content query --uri content://...
content insert --uri content://...
```


# SETTINGS
```
settings list system
settings put global airplane_mode_on 1
```


# RECORDING
```
screencap /sdcard/screen.png
screenrecord /sdcard/video.mp4
```


# SECURITY CHECKS
```
getprop ro.debuggable
getprop ro.secure
settings get global adb_enabled
```
