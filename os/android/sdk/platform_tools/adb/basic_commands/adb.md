# GENERALLY
```
adb --help
adb devices
adb version
adb shell
```



# NETWORK
```
adb connect IP:PORT
adb disconnect
adb forward tcp:8080 tcp:8080
adb reverse tcp:8080 tcp:8080
```



# INSTALL
```
adb install app.apk
adb install -r app.apk        # überschreiben (update)
adb uninstall com.app.name
```



# TRANSFER DATA
```
adb push local.txt /sdcard/
adb pull /sdcard/file.txt
adb pull /sdcard/Download/
```



# LOGS
```
adb logcat
adb logcat -d > logs.txt
adb logcat | grep keyword
adb logcat -c
```



# EXECUTE
```
adb shell monkey -p com.app.name -c android.intent.category.LAUNCHER 1
```



# RECORDING
```
adb exec-out screencap -p > screen.png
adb exec-out screenrecord --time-limit 10 - > video.mp4
```



# DEBUGGING
```
adb bugreport > report.zip
adb get-state
adb get-serialno
```



# BACKUP
```
adb backup -apk -shared -all -f backup.ab
```
- deactiveted on actal devices



# FLAGS
`-s DEVICE_ID <command>` specifys the device



# ROOT NEEDED
```
adb root
adb remount             # /system writeable
```
