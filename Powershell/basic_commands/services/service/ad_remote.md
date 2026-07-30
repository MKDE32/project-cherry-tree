# AD REMOTE
```
get-service -ComputerName GOOGLE-ICL-DC
Get-Service -ComputerName GOOGLE-ICL-DC | Where-Object {$_.Status -eq "Running"}
invoke-command -ComputerName GOOGLE-ICL-DC,LOCALHOST -ScriptBlock {Get-Service -Name 'windefend'}
```
