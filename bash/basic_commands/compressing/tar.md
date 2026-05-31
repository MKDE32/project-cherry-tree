.tar ist wohl mit .zip dateien von windows vergleichbar, hier beispielsweise mit Java.
 Die Versionen vom RPM Package Management sind  etwas kleiner, benötigen aber ein RPM-Installationsprogramm. Wir wollen  im Folgenden mit dem TAR-Archiv arbeiten. Zunächst ist zu überlegen, wo Java am besten aufgehoben ist. Das Verzeichnis /opt/java ist ein guter Kandidat, vorausgesetzt, wir haben die Zugriffsrechte. Zuerst ist eine Version von Linux herunterzuladen, etwa jdk-8u65-linux-x64.tar.gz. Wir setzen das Archiv in das gewünschte Verzeichnis. Anschließend wird es im gleichen Verzeichnis ausgepackt:
            
            $ cd /opt/java
			$ ls
			jdk-8u65-linux-x64.tar.gz
			$ tar xvzf jdk-8u65-linux-x64.tar.gz

Es entsteht ein Unterverzeichnis jdk1.8.0 mit der kompletten Installation, die das Java-Home bildet. Die tar.gz-Datei kann gelöscht werden.
Damit Compiler und JVM gefunden werden, sollte der Suchpfad um das bin-Verzeichnis des JDK erweitert werden:
            
            $ export JAVA_HOME=/opt/java/jdk1.8.0
			$ PATH=$JAVA_HOME/bin:$PATH
