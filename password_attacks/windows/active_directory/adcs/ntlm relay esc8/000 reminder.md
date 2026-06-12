- adcs can occur by web enrollment
- if so, it uses only http


[ Angreifer ]
      │
      │ forces to auth
      ▼
[ Domain Controller ]
      │
      │ NTLM Auth
      ▼
[ Angreifer (Relay) ]
      │
      │ forwards
      ▼
[ CA (AD CS Web Enrollment) ]
      │
      │ issues a cert
      ▼
[ Angreifer bekommt Zertifikat als DC ]
