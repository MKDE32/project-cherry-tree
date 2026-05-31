function

name() 
	{
	<commands>
	}



funktionen aufrufen:

case $opt in
	"1") network_range ;;
	"2") ping_host ;;
	"3") network_range && ping_host ;;
	"*") exit 0 ;;
esac
