# info
super website: `regex.com`

# example
```
'(https?://[^']+)'
```





# Regular Expression / Expression flag
/ sets start and end of regular expression
/RegularExpression/ExpressionFlag





# Character
Buchstaben
abc

Sonderzeichen
._% +-@

großes und kleines a
[Aa]

Letzte drei Zeichen sind Zahlen 1-9
[0-9][0-9][0-9]$

Matches a .
\.

Gruppierung: T oder t
(T|t)

any character except line breaks
.

matches any digit 0-9
\d

matches all alphanumeric + underscore
\w

not
\W

matches all white space
\s

not
\S





# Range
a-z Lowecase
[a-z]

A-Z Uppercase
[A-Z]

0-9
[0-9]





# Beginning / End
lines that begin with
^Wort

lines end with
Wort$

outputs blank lines
^$





# Quantifier
0 or more of the preceding token
*

1 or more of the preceding token
+

between 0 and 1 of the preceding token
?

matches 2-4 of the preceding token
{2-4}





# Look Behind
positive look behind
(?<=the).
markiert was nach der klammer steht nach dem Ausdruck in der look behind klammer

negative look behind
(?<!the).
inverted

positive look ahead
.(?=he)
markiert was vor der klammer steht nach dem Ausdruck in der look behind klammer

negative look ahead
.(?!he)
inverted





------------------------------------------------------------------------------
------------------------------------------------------------------------------
# Flags

global search
g

ignore case sensetivity
i

multiline
m
^ / $ will match the start / end of the line

dotall
s
dot also matches newline
