# Trainiere-dein-musikalisches-Geh-r
Programm zur Gehörbildung bei verschiedenen Tonleitern

Installation Linux:

1. tar entpacken.
2. Ordner im Terminal öffnen.
3. Befehl 
	batch installation_linux.sh
   ausführen.
   Alternativ können die Pythonmodule auch manuell installiert werden.
4. Zum Starten des Programmes
	python3 main.py
   ausführen.


Installation Windows:

1. zip-Datei entpacken.
2. Python3 installieren.
3. installation_windows.bat durch Doppelklick ausführen.
4. Zum Starten start.bat durch Doppelklick ausführen.

Benutzung:

Das Quiz kann durch Klicken auf Start begonnen werden.
Das Fenster, das zu Beginn geöffnet wird, bietet zudem verschiedene Einstellmöglichkeiten.
Im rechten Drittel kann man einstellen, wie viele Fragen gestellt werden sollen, wie viele Töne abgespielt werden sollen, ob die Töne nacheinander (Melodietest), gleichzeitig (Harmonietest) oder als Akkordfolge (Melodie- und Harmonietest) abgespielt werden sollen. Die Anzahl der Melodie- und Harmonietöne muss separat eingestellt werden.
Des Weiteren kann der Frequenzbereich, in dem sich die Töne aufhalten sollen, eingestellt werden.
In der Tabelle kann eingestellt werden, wie viele Sekunden der jeweilige Ton bzw. Akkord klingen soll. Durch Einstellungen speichern kann die Anzahl der Töne in der Tabelle aktualisiert werden. 
Die Option Preset hat (noch) keine Funktion.
Es können die Intervalle, die vorkommen sollen, durch Zahlen angegeben werden. Diese geben bei 12-tonleitern die Anzahl der Halbtonschritte der zu testenden Intervalle an. Bei der Mikrotonalen Tonleiter geben die Zahlen die Anzahl der Vierteltöne an. Bei allen anderen Tonleitern die Anzahl der Tonschritte zum nächsten Ton.
Die Tonleiter kann in der Mitte des Fensters eingestellt werden. Es gibt einige vorgefertigte Tonleitern. Es kann jedoch auch eine individuelle Tonleiter kreiert werden. 
Im linken Drittel kann die Klangfarbe der Töne eingestellt werden. Das Obertonspektrum kann dabei frei verändert werden. Es gibt auch hier einige Presets. Durch Klicken auf 'Vorhören' kann der Ton vor dem Test angehört werden, um zu entscheiden, ob die Klangfarbe zusagt.

Klickt man auf 'Start' beginnt der Test und es werden Töne entsprechend den Einstellungen abgespielt. In die leeren Felder müssen die Intervalle als Zahlen eingegeben werden. Hat man dies getan, muss man auf Eingabe bestätigen klicken und erhält eine Rückmeldung darüber, welche Intervalle richtig (grün) und welche falsch (rot) eingegeben wurden. Durch 'weiter' kommt man zur nächsten Frage.
