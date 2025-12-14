 FlashcardsPP - Flashcards Python Project (Console)
 --------------------------------------------------

Ziel dieses Projekts ist es:
• Den vollständigen Prozess von der Problemanalyse bis zur Implementierung zu verstehen und anzuwenden
• Grundlegende Python-Programmierkonzepte anzuwenden, die im Modul Programming Foundations erlernt wurden
• Die Demonstration der Verwendung von Konsoleninteraktionen, Datenvalidierung und Dateiverarbeitung
• Einen sauberen, gut strukturierten und dokumentierten Code zu erstellen
• Die Studierenden auf Teamarbeit und Dokumentation in späteren Modulen vorzubereiten
• Dieses Repository als Ausgangspunkt zu verwenden, indem du es in dein eigenes GitHub-Konto importierst
• Ausschliesslich in deiner eigenen Kopie arbeiten — führe keine Änderungen im ursprünglichen Template durch
• Regelmässige Commits durchführen, um deinen Fortschritt nachzuverfolgen

|Analyse|

Problem
- Viele Studierende lernen mit Karteikarten. Papierkarten sind jedoch unpraktisch: Sie sind Zeitaufwendig in der Vorbereitung, können verloren gehen, schwer gemischt werden und bieten keine Auswertung der Lernergebnisse.

Lösung
- Das Ziel des Projekts ist die Entwicklung einer digitalen Quiz-Anwendung,
die das Lernen mit Karteikarten vereinfacht und modernisiert. User können
Fragen aus verschiedenen Kapiteln auswählen, erhalten direktes Feedback zu
ihren Antworten und sehen am Ende eine Auswertung ihrer Ergebnisse. Durch
die Speicherung im Leaderboard wird das Lernen interaktiv, motivierend und
eﬀizient gestaltet.

User stories: 
1. Als User möchte ich beim Start einen Benutzernamen eingeben. 
2. Als User möchte ich einen Hinweis erhalten, wenn der Benutzername schon vergeben ist. 
3. Als User möchte ich spezifische oder alle Kapitel auswählen. 
4. Als User möchte ich die Anzahl der Fragen auswählenn zwischen 10, 20 oder 30 Fragen.
5. Als User möchte ich eine zufällige Reihenfolge der Fragen gestellt bekommen. 
6. Als User möchte ich pro Frage vier Antwortoptionen sehen, wobei nur eine Antwort korrekt ist. 
7. Als User möchte ich während einer Session keine Frage doppelt gestellt bekommen. 
8. Als User möchte ich sofort ein Feedback (richtig/7falsch) erhalten. 
9. Als User möchte ich das Quiz vorzeitig abbrechen können 
10. Als User möchte ich am Ende eine Auswertung mit Punktzahl und Zeitstempel sehen. 
11. Als User möchte ich ein Leaderboard sehen. 
12. Als User möchte ich, dass meine Session im Leaderboard gespeichert wird.

Use cases: 
- Eingabe Username 
- Auswahl des Themengebiets 
- Auswahl Anzahl der Fragen 
- Präsentierung der einzelnen Fragen 
- Validierung der eingegebenen Antworten 
- Beendigung des Quiz (regulär oder durch Abbruch) 
- Erstellung der Auswertung 
- Speicherung des Ergebnisses im Leaderboard 
- Anzeige des aktuellen Leaderboards


|Projektanforderungen|

1. Interaktive Anwendung (Konsolen Eingabe)

Das Programm läuft vollständig über die Konsole. Der Anwender kann:

• sich anmelden mit einem Benutzernamen
• Eingabe von einzelnen oder von allen gewünschten Kapiteln
• Auswahl der gewünschten Anzahl an Fragen
• Fragen beantworten und gleich das Resultat erhalten
• Möglichkeit Quiz abzubrechen inkl. Auswertung bisheriger Beantwortung
• Auswertung der Antworten
• Anzeige eines Leaderboards

2. Datenvalidierung

Die Anwendung validiert alle Benutzereingaben, um die Datenintegrität und eine reibungslose Benutzererfahrung zu gewährleisten. Dies wird in main.py wie folgt implementiert:

• Es validiert, ob ein Benutzername schon erfasst ist oder nicht
• Es validiert, ob der Benutzername aus mindestens fünf Zeichen besteht und davon mindestens ein Buchstaben und eine Zahl beinhaltet sowie kein Leerzeichen im Benutzername vorhanden sein darf
• Es validiert, ob die vorgeschlagenen Kapiteln ausgewählt werden
• Es validiert, ob die vorgeschlagenen Fragen ausgewählt werden
• Es validiert, ob die Antwort auch entsprechend einer der Antwortmöglichkeiten entspricht

3. Dateiverarbeitung

Das Programm speichert alle relevanten Daten in einer JSON-Datei.

Input:
   • Die Fragen und dazugehörigen Antworten wurden mit ChatGPT erstellt, nachdem man die Unterrichtsfolien ihm vorgegeben hat

Output:
   • Nachdem das Quiz beendet wurde, wird eine persönliche Auswertung & ein Leaderboard erstellt

|Implementierung|

Technologie
• Programmiersprache:  Python 3.11.14
• Entwicklungsmgebung: GitHub Codespaces/Visual Studio Code
• Externe Plattformen: ChatGPT - Fragen erstellt
• Formatierung: PEP8-konform

Projektstruktur

My_Project_Flashcards
├── main.py                  # Programmlogik (Startpunkt der Konsolenanwendung)
├── username_setup.py        # Verwaltung und Validierung der Benutzernamen
├── quiz_setup.py            # Vorbereitung und Konfiguration des Quiz
├── quiz_run.py              # Durchführung des Quiz (Fragen anzeigen, Antworten prüfen)
├── results_leaderboard.py   # Auswertung der Ergebnisse und Verwaltung des Leaderboards
├── leaderboard.json         # Speicherung der Quiz-Ergebnisse und Bestenliste
├── questions.json           # Fragenkatalog des Quiz (Kapitel, Fragen, Antworten)
└── README.md  

|Starten der Anwendung|

https://github.com/albintahiri17-dot/my_project_flashcards.git

1. Das Projekt „my_project_flashcards“ von GitHub herunterladen und als Projektordner ablegen. 
2. In der Python-Konsole mit cd in den Projektordner my_project_flashcards wechseln.
3. Die Datei main.py ausführen.

Team    	    Beitrag
Fabian Vokrraj	Username, Leaderboard & Flashcards
Albin Tahiri	Kategorien, Menüführung & Korrektur
Amir Muliqi 	Quiz-Logik, Validierung & Zusammenhänge

|Beitrag|
• Verwende dieses Repository als Ausgangspunkt, indem du es in dein eigenes GitHub-Konto importierst.
• Arbeite ausschließlich in deiner eigenen Kopie – füge keine Änderungen in die ursprüngliche Vorlage ein.
• Führe regelmäßig Commits durch, um deinen Fortschritt nachzuverfolgen.

|Lizenz|
Dieses Projekt wird ausschliesslich zu Bildungszwecken im Rahmen des
Moduls Programmierung Grundlagen bereitgestellt. MIT License