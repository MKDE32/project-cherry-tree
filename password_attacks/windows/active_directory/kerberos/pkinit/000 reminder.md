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
- if a user has write permission over the `msds-keycredentiallink` of another user
- he can take control over that user











