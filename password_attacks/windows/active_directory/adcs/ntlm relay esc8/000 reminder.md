- adcs can occur by web enrollment
- if so, it uses only http

```
       [ attacker ]
             │
             │ forces to auth
             ▼
          [ dc ]
             │
             │ NTLM Auth
             ▼
        [ attacker ]
             │
             │ forwards
             ▼
[ CA (AD CS Web Enrollment) ]
             │
             │ issues a cert
             ▼
[ attackert gets cert as dc ]
```
