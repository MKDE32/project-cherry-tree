
```
Sub Workbook_Open()

	Set WshShell = CreateObject("Wscript.Shell")

	Set WshShellExec = WshShell.Exec("whoami")

	MsgBox (WshShellExec.StdOut.ReadAll)

End Sub
```

