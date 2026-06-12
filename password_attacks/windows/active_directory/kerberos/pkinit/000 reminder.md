# public key cryptographie for initial authentication
```
Client
  │
  │ 1. Login Request (PKINIT)
  ▼
KDC (Domain Controller)
  │
  │ 2. Verify Private Key proof
  │
  │ 3. Check Public Key in AD
  ▼
OK?
  │
  ▼
4. Issue TGT
```

- Client besitzt ein Schlüsselpaar
- Private Key (bleibt beim Client)
- Public Key (im AD gespeichert oder via Zertifikat)
- Der Domain Controller stellt den
- Key Distribution Center bereit











