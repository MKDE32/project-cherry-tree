KOMMENTAR
REM

VERZÖGERUNG GLOBAL
DEFAULT_DELAY XXXX
(Einmalig am Anfang angeben)

VERZÖGERUNG
DELAY XXXX

ZEICHENFOLGE
STRING XXXXXXX

WINDOWS KEY
GUI X

MENÜ
MENU

SHIFT
SHIFT XXXXX

ALT
ALT XXXXX

CONTROL
CTRL

ARROW KEYS
DOWN
LEFT
RIGHT
UP

WIEDERHOLEN
REPEAT XXXX
(Number of times to repeat the previous command)

---------------------------------------------------------------------

COMPILING
mit "duckencoder":

usage: duckencode -i [file ..]			encode specified file
or: duckencode -i [file ..] -o [file ..]	encode to specified file

EXAMPLE ON LINUX SYSTEM
java -jar duckencoder.jar -i exploit.txt -o /media/microsdcard/inject.bin
