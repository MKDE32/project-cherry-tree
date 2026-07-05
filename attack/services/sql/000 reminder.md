# sql versions & clients

| SGBD        | Port par défaut | OS cible typique      | Client principal        | Authentification        | Notes pentest clés |
|------------|----------------|----------------------|------------------------|-------------------------|-------------------|
| MySQL      | 3306           | Linux / Windows      | mysql                  | User/Password           | Bruteforce fréquent, fichiers via LOAD_FILE, UDF possible |
| MariaDB    | 3306           | Linux                | mysql                  | User/Password           | Très proche de MySQL, mêmes vecteurs |
| PostgreSQL | 5432           | Linux                | psql                   | User/Password / Cert    | Command execution via COPY TO PROGRAM |
| MSSQL      | 1433           | Windows              | sqlcmd                 | Windows Auth / SQL Auth | xp_cmdshell, SMB relay, AD intégré |
| Oracle DB  | 1521           | Linux / Unix         | sqlplus                | User/Password           | SID enumeration, TNS listener abuse |
| SQLite     | N/A (fichier)  | Linux / Windows      | sqlite3                | Aucun (fichier)         | Accès direct au fichier DB |
| Redis      | 6379           | Linux                | redis-cli              | Optionnelle             | Pas vraiment SQL, RCE via config write |
| MongoDB    | 27017          | Linux / Windows      | mongo / mongosh        | Optionnelle             | NoSQL, souvent exposé sans auth |

