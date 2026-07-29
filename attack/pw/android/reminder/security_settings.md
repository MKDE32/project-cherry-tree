# BASIC COMMAND
```
getprop
```

# FLAGS
## VERY CRITICAL
- `ro.debuggable=1`
  - `0` = normal
  - `1` = debugable, unsecure
- `ro.secure=0`
  - `1` = normal / secure mode
  - `0` = device in debugmode, very unsecure
- `ro.build.type`
  - `user` = normale release
  - `userdebug` = half-open (dev)
  - `eng` = engineering build (very unsafe)
- `ro.build.tags`
  - `release-keys` = normal secure
  - `test-keys` = not safe firmware / custom ROM
- `ro.adb.secure`
  - `1` = ADB braucht Auth
  - `0` = unsecure ADB-connection possible
- `ro.build.selinux`
  - `enforcing` safe
  - `permissive` less safe
- `ro.boot.verifiedbootstate`
  - `green` verified boot
  - `orange` unlocked bootloader
  - `red` compromised
- `ro.boot.flash.locked`
  - bootloader locked / unlocked
- `ro.boot.vbmeta.device_state`
  - verified boot state




## ATTACK SURFACE
- `ro.kernel.qemu`
  - `1` = Emulator
  - `0` = real hardware
- `ro.build.version.release`
  - android version
- `ro.build.version.sdk`
  - api level
- `ro.build.version.security_patch`
  - shows security updates
- `ro.build.fingerprint`
  - shows firmware build

## INFO
- `ro.product.model`
  - vendor infos
- `ro.product.manufacturer`
  - vendor infos
- `persist.sys.usb.config`
  - adb exposure level
- `sys.usb.state`
  - usb debug active?







