extrahiert key.pem und cert.pem aus der .pfx (PKCS#12-Datei) datei
openssl pkcs12 -in legacyy_dev_auth.pfx -nocerts -out key.pem -nodes
openssl pkcs12 -in legacyy_dev_auth.pfx -nokeys -out cert.pem
Viele Anwendungen (z. B. Apache, Nginx, Docker, Kubernetes, OAuth, mTLS) erwarten:
privaten Schlüssel → key.pem und Zertifikat → cert.pem getrennt voneinander
Windows/IIS nutzt dagegen oft direkt die .pfx.
