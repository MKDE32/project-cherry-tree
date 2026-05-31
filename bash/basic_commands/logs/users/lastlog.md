lists users who have not logged in in the past 90 days
lastlog -b 90

lists users who have not logged in in the past 90 days. Filtered by grep and tail.
lastlog -b 90 | tail -n 5 | grep -v 'Never logg'
