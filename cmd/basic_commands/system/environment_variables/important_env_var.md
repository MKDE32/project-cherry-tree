A
--------------------------------------------
ALLUSERSPROFILE
-> Shared system data (C:\ProgramData)

APPDATA
-> Roaming user data (often contains credentials, configs)

--------------------------------------------
C
--------------------------------------------
COMPUTERNAME
-> Hostname (useful for network enumeration)

COMSPEC
-> Path to cmd.exe (useful for detection of environment changes)

--------------------------------------------
H
--------------------------------------------
HOMEDRIVE
-> User drive mapping

HOMEPATH
-> User directory path

--------------------------------------------
L
--------------------------------------------
LOCALAPPDATA
-> Local app storage (often contains tokens, cache, secrets)

%LOGONSERVER%
-> Provides us with the login server for the currently active user followed by the machine's hostname.
We can use this information to know if a machine is joined to a domain or workgroup.

--------------------------------------------
O
--------------------------------------------
OS
-> OS identification

--------------------------------------------
P
--------------------------------------------
PATH
-> Command execution path (hijacking vector if misconfigured)

PATHEXT
-> Determines executable file types (attack surface for extension abuse)

PROCESSOR_ARCHITECTURE
-> Architecture validation for payload compatibility

%ProgramFiles%
-> Equivalent of C:\Program Files. This location is where all the programs are installed on an x64 based system.

%ProgramFiles(x86)%
-> Equivalent of C:\Program Files (x86). This location is where all 32-bit programs running under WOW64 are installed. Note that this variable is only accessible on a 64-bit host. It can be used to indicate what kind of host we are interacting with. (x86 vs. x64 architecture)




--------------------------------------------
S
--------------------------------------------
SYSTEMDRIVE
-> System root drive (useful for file system targeting)

SYSTEMROOT
-> Windows system directory (C:\Windows)

--------------------------------------------
U
--------------------------------------------
USERNAME
-> Current user context (privilege level check)

USERPROFILE
-> Full user directory (primary target for enumeration)

--------------------------------------------
W
--------------------------------------------
WINDIR
-> Windows directory (often used in LOLBins pathing)

--------------------------------------------

SECURITY NOTES:
- PATH misconfigurations can allow DLL / binary hijacking
- APPDATA and LOCALAPPDATA often contain credentials or tokens
- USERNAME + USERPROFILE are key for privilege context mapping
- SYSTEMROOT/WINDIR are frequently used in LOLBins execution paths
