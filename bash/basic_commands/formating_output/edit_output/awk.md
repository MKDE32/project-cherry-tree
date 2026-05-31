awk {anweisung}
gibt nur die erste spalte aus
cat /etc/hosts | awk ‘{print $1}’

awk Bedingung { Anweisungen }
wenn erste spalte 127.0.0.1 dann ausgabe erste und zweite spalte
awk '$1 == "127.0.0.1" { print $1,$2 }' /etc/hosts
oder mit der pipe
cat /etc/hosts | awk '$1 == "127.0.0.1" { print $1,$2 }'
