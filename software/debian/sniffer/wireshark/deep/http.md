# HTTP Analysis

| Purpose | Filter |
|----------|--------|
| HTTP Requests | `http.request` |
| HTTP Responses | `http.response` |
| GET Requests | `http.request.method == "GET"` |
| POST Requests | `http.request.method == "POST"` |
| User-Agent Header | `http.user_agent` |
| HTTP Errors | `http.response.code >= 400` |



# TLS / HTTPS Analysis

| Purpose | Filter |
|----------|--------|
| TLS Traffic | `tls` |
| Client Hello | `tls.handshake.type == 1` |
| Server Hello | `tls.handshake.type == 2` |
| SNI Hostname | `tls.handshake.extensions_server_name` |
| Certificate Exchange | `tls.handshake.certificate` |






