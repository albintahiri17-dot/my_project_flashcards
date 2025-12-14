 FlashcardsPP - Flashcards Python Project (Console)
 --------------------------------------------------

Ziel dieses Projekts ist es:
• Den vollständigen Prozess von der Problemanalyse bis zur Implementierung zu verstehen und anzuwenden
• Grundlegende Python-Programmierkonzepte anzuwenden, die im Modul Programming Foundations erlernt wurden
• Demonstriere die Verwendung von Konsoleninteraktionen, Datenvalidierung und Dateiverarbeitung
• Einen sauberen, gut strukturierten und dokumentierten Code zu erstellen
• Die Studierenden auf Teamarbeit und Dokumentation in späteren Modulen vorbereiten
• Dieses Repository als Ausgangspunkt verwenden, indem du es in dein eigenes GitHub-Konto importierst
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

1. Interaktive App (Konsolen Eingabe)

User können:
• Eingabe von einzelnen oder von allen gewünschten Kapiteln
• Auswahl der gewünschten Anzahl an Fragen
• Fragen beantworten und gleich das Resultat erhalten
• Möglichkeit Quiz abzubrechen inkl. Auswertung bisheriger Beantwortung
• Auswertung der Antworten
• Anzeige eines Leaderboards

2. Datenvalidierung
• Es wird validiert, ob der Username schon vorhanden ist oder nicht
• Es wird validiert, ob die Antwort auch entsprechend einer der Antwortmöglichkeiten entspricht

3. Dateiverarbeitung
• Nachdem das Quiz beendet wurde, wird eine persönliche Auswertung erstellt
• Nachdem man die Auswertung speichert, wird das Leaderboard erstellt/ergänzt und angezeigt


|Implementierung|

Technologie
• Python 3.x
• Umgebung: GitHub Codespaces
• Die Fragen werden ChatGPT erstellt

|Team|
|Fabian Vokrraj|
|Albin Tahiri|
|Amir Muliqi|

|Beitrag|
• Verwende dieses Repository als Ausgangspunkt, indem du es in dein eigenes GitHub-Konto importierst.
• Arbeite ausschließlich in deiner eigenen Kopie – füge keine Änderungen in die ursprüngliche Vorlage ein.
• Führe regelmäßig Commits durch, um deinen Fortschritt nachzuverfolgen.

|Lizenz|
Dieses Projekt wird ausschliesslich zu Bildungszwecken im Rahmen des
Moduls Programmierung Grundlagen bereitgestellt. MIT License