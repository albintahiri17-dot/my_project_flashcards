<<<<<<< HEAD
# 🃏 FlashcardsPP – Flashcard Web-Applikation

> Eine browserbasierte Flashcard-Quiz-Applikation, entwickelt mit NiceGUI, SQLAlchemy und SQLite.  
> Migration des CLI-basierten FlashcardsPP-Projekts zu einer vollständigen Web-Applikation.
=======
# FlashcardsPP - Flashcards Python Project (Console)

Ziel dieses Projekts ist es:

- Den vollständigen Prozess von der Problemanalyse bis zur Implementierung zu verstehen und anzuwenden
- Grundlegende Python-Programmierkonzepte anzuwenden, die im Modul Programming Foundations erlernt wurden
- Die Demonstration der Verwendung von Konsoleninteraktionen, Datenvalidierung und Dateiverarbeitung
- Einen sauberen, gut strukturierten und dokumentierten Code zu erstellen
- Die Studierenden auf Teamarbeit und Dokumentation in späteren Modulen vorzubereiten
- Dieses Repository als Ausgangspunkt zu verwenden, indem du es in dein eigenes GitHub-Konto importierst
- Ausschliesslich in deiner eigenen Kopie arbeiten — führe keine Änderungen im ursprünglichen Template durch
- Regelmässige Commits durchführen, um deinen Fortschritt nachzuverfolgen
>>>>>>> d278fc92bbb7a9fdc180c44b3987b06c30e988cd

---

<<<<<<< HEAD
## 📝 Anforderungen

### Problem

Viele Studierende lernen mit Karteikarten. Papierkarten sind jedoch unpraktisch: Sie sind zeitaufwendig in der Vorbereitung, können verloren gehen, sind schwer zu mischen und bieten keine Auswertung der Lernergebnisse.

### Lösung
=======
**Problem**

- Viele Studierende lernen mit Karteikarten. Papierkarten sind jedoch unpraktisch: Sie sind Zeitaufwendig in der Vorbereitung, können verloren gehen, schwer gemischt werden und bieten keine Auswertung der Lernergebnisse.

**Lösung**

- Das Ziel des Projekts ist die Entwicklung einer digitalen Quiz-Anwendung,
  die das Lernen mit Karteikarten vereinfacht und modernisiert. User können
  Fragen aus verschiedenen Kapiteln auswählen, erhalten direktes Feedback zu
  ihren Antworten und sehen am Ende eine Auswertung ihrer Ergebnisse. Durch
  die Speicherung im Leaderboard wird das Lernen interaktiv, motivierend und
  eﬀizient gestaltet.

---

## 📖 User Stories

### 1. Eingabe Benutzername

**Als User möchte ich beim Start einen Benutzernamen eingeben.**

- **Inputs:** Benutzername (`string`)
- **Outputs:** bestätigter Benutzername / Fehlermeldung

---

### 2. Benutzername bereits vergeben

**Als User möchte ich einen Hinweis erhalten, wenn der Benutzername schon vergeben ist.**

- **Inputs:** Benutzername (`string`)
- **Outputs:** Verfügbarkeitsstatus, Fehlermeldung

---

### 3. Kapitel auswählen

**Als User möchte ich spezifische oder alle Kapitel auswählen.**

- **Inputs:** Kapitel-Auswahl (`list[int]` | `all`)
- **Outputs:** ausgewählte Kapitel

---

### 4. Anzahl Fragen wählen

**Als User möchte ich die Anzahl der Fragen auswählen zwischen 10, 20 oder 30 Fragen.**

- **Inputs:** Anzahl Fragen (`int`)
- **Outputs:** ausgewählte Anzahl Fragen

---

### 5. Zufällige Reihenfolge

**Als User möchte ich eine zufällige Reihenfolge der Fragen gestellt bekommen.**

- **Inputs:** Fragenpool (`list[Question]`)
- **Outputs:** zufällig sortierte Fragen (`list[Question]`)

---

### 6. Antwortoptionen anzeigen

**Als User möchte ich pro Frage vier Antwortoptionen sehen, wobei nur eine Antwort korrekt ist.**

- **Inputs:** Frage (`Question`)
- **Outputs:** Antwortoptionen (`list[Answer]`)

---

### 7. Keine doppelten Fragen

**Als User möchte ich während einer Session keine Frage doppelt gestellt bekommen.**

- **Inputs:** bisherige Fragen (`list[Question]`)
- **Outputs:** neue, noch nicht gestellte Frage

---

### 8. Sofortiges Feedback

**Als User möchte ich sofort ein Feedback (richtig/falsch) erhalten.**

- **Inputs:** gewählte Antwort (`Answer`)
- **Outputs:** Feedback (`richtig` | `falsch`)

---

### 9. Quiz abbrechen

**Als User möchte ich das Quiz vorzeitig abbrechen können.**

- **Inputs:** Abbruchaktion (`boolean`)
- **Outputs:** beendete Session, Zwischenstand

---

### 10. Auswertung anzeigen

**Als User möchte ich am Ende eine Auswertung mit Punktzahl und Zeitstempel sehen.**

- **Inputs:** Antworten, Zeit (`list[Answer]`, `timestamp`)
- **Outputs:** Punktzahl, Zeitstempel

---

### 11. Leaderboard anzeigen

**Als User möchte ich ein Leaderboard sehen.**

- **Inputs:** none
- **Outputs:** Rangliste (`list[UserScore]`)

---

### 12. Session speichern

**Als User möchte ich, dass meine Session im Leaderboard gespeichert wird.**

- **Inputs:** Benutzername, Punktzahl (`string`, `int`)
- **Outputs:** aktualisiertes Leaderboard

---

**Use cases**

- Eingabe Username
- Auswahl des Themengebiets
- Auswahl Anzahl der Fragen
- Präsentierung der einzelnen Fragen
- Validierung der eingegebenen Antworten
- Beendigung des Quiz (regulär oder durch Abbruch)
- Erstellung der Auswertung
- Speicherung des Ergebnisses im Leaderboard
- Anzeige des aktuellen Leaderboards
>>>>>>> d278fc92bbb7a9fdc180c44b3987b06c30e988cd

FlashcardsPP ist eine digitale Quiz-Applikation, die das Lernen mit Karteikarten vereinfacht und modernisiert. Benutzer können Fragen aus verschiedenen Kapiteln auswählen, erhalten direktes Feedback zu ihren Antworten und sehen am Ende eine Auswertung ihrer Ergebnisse. Durch die Speicherung im Leaderboard wird das Lernen interaktiv, motivierend und effizient gestaltet.

---

## 📖 User Stories

<<<<<<< HEAD
### 1. Benutzername eingeben
**Als User möchte ich beim Start einen Benutzernamen eingeben.**
- **Inputs:** Benutzername (`string`)
- **Outputs:** Bestätigter Benutzername / Fehlermeldung
=======
- sich anmelden mit einem Benutzernamen
- Eingabe von einzelnen oder von allen gewünschten Kapiteln
- Auswahl der gewünschten Anzahl an Fragen
- Fragen beantworten und gleich das Resultat erhalten
- Möglichkeit Quiz abzubrechen inkl. Auswertung bisheriger Beantwortung
- Auswertung der Antworten
- Anzeige eines Leaderboards
>>>>>>> d278fc92bbb7a9fdc180c44b3987b06c30e988cd

---

### 2. Benutzername bereits vergeben
**Als User möchte ich einen Hinweis erhalten, wenn der Benutzername bereits vergeben ist.**
- **Inputs:** Benutzername (`string`)
- **Outputs:** Verfügbarkeitsstatus, Fehlermeldung

<<<<<<< HEAD
---
=======
- Es validiert, ob ein Benutzername schon erfasst ist oder nicht
- Es validiert, ob der Benutzername aus mindestens fünf Zeichen besteht und davon mindestens ein Buchstaben und eine Zahl beinhaltet sowie kein Leerzeichen im Benutzername vorhanden sein darf
- Es validiert, ob die vorgeschlagenen Kapiteln ausgewählt werden
- Es validiert, ob die vorgeschlagenen Fragen ausgewählt werden
- Es validiert, ob die Antwort auch entsprechend einer der Antwortmöglichkeiten entspricht
>>>>>>> d278fc92bbb7a9fdc180c44b3987b06c30e988cd

### 3. Kapitel auswählen
**Als User möchte ich spezifische oder alle Kapitel auswählen.**
- **Inputs:** Kapitel-Auswahl (`list[int]` | `all`)
- **Outputs:** Ausgewählte Kapitel

---

<<<<<<< HEAD
### 4. Anzahl Fragen wählen
**Als User möchte ich die Anzahl der Fragen auswählen: 10, 20 oder 30.**
- **Inputs:** Anzahl Fragen (`int`)
- **Outputs:** Ausgewählte Anzahl Fragen

---
=======
**Input:**

- Die Fragen und dazugehörigen Antworten wurden mit ChatGPT erstellt, nachdem man die Unterrichtsfolien ihm vorgegeben hat

**Output:**

- Nachdem das Quiz beendet wurde, wird eine persönliche Auswertung & ein Leaderboard erstellt
>>>>>>> d278fc92bbb7a9fdc180c44b3987b06c30e988cd

### 5. Zufällige Reihenfolge
**Als User möchte ich die Fragen in einer zufälligen Reihenfolge gestellt bekommen.**
- **Inputs:** Fragenpool (`list[Question]`)
- **Outputs:** Zufällig sortierte Fragen (`list[Question]`)

<<<<<<< HEAD
---
=======
**Technologie**

- Programmiersprache: Python 3.11.14
- Entwicklungsmgebung: GitHub Codespaces/Visual Studio Code
- Externe Plattformen: ChatGPT - Fragen erstellt
- Formatierung: PEP8-konform
>>>>>>> d278fc92bbb7a9fdc180c44b3987b06c30e988cd

### 6. Antwortoptionen anzeigen
**Als User möchte ich pro Frage vier Antwortoptionen sehen, wobei nur eine Antwort korrekt ist.**
- **Inputs:** Frage (`Question`)
- **Outputs:** Antwortoptionen (`list[Answer]`)

---

### 7. Keine doppelten Fragen
**Als User möchte ich während einer Session keine Frage doppelt gestellt bekommen.**
- **Inputs:** Bisherige Fragen (`list[Question]`)
- **Outputs:** Neue, noch nicht gestellte Frage

---

### 8. Sofortiges Feedback
**Als User möchte ich sofort ein Feedback (richtig/falsch) erhalten.**
- **Inputs:** Gewählte Antwort (`Answer`)
- **Outputs:** Feedback (`richtig` | `falsch`)

---

### 9. Quiz abbrechen
**Als User möchte ich das Quiz vorzeitig abbrechen können.**
- **Inputs:** Abbruchaktion (`boolean`)
- **Outputs:** Beendete Session, aktueller Zwischenstand

---

### 10. Auswertung anzeigen
**Als User möchte ich am Ende eine Auswertung mit Punktzahl und Zeitstempel sehen.**
- **Inputs:** Antworten, Zeit (`list[Answer]`, `timestamp`)
- **Outputs:** Punktzahl, Zeitstempel

---

### 11. Leaderboard anzeigen
**Als User möchte ich ein Leaderboard sehen.**
- **Inputs:** keine
- **Outputs:** Rangliste (`list[UserScore]`)

---

### 12. Session speichern
**Als User möchte ich, dass meine Session im Leaderboard gespeichert wird.**
- **Inputs:** Benutzername, Punktzahl (`string`, `int`)
- **Outputs:** Aktualisiertes Leaderboard

---

## 🧩 Use Cases

### Haupt-Use-Cases
- Benutzername eingeben (Registrierung / Login)
- Kapitel auswählen
- Anzahl der Fragen auswählen
- Fragen einzeln präsentieren
- Antworten validieren
- Quiz beenden (regulär oder Abbruch)
- Auswertung anzeigen
- Ergebnis im Leaderboard speichern
- Leaderboard anzeigen

### Akteure
- **User** – nimmt am Quiz teil, sieht Ergebnisse und Leaderboard

---

## 🏛️ Architektur

### Schichten
- **UI-Schicht (`views/`):** NiceGUI browserbasierte Oberfläche – keine Businesslogik
- **Service-Schicht (`services/`):** Gesamte Businesslogik als OOP-Klassen
- **Persistenzschicht (`models/`):** SQLite-Datenbank über SQLAlchemy ORM

### Design-Entscheidungen
- Strikte 3-Schichten-Trennung: views ↔ services ↔ models
- Kein rohes SQL – alle Datenbankzugriffe über SQLAlchemy ORM
- NiceGUI serverseitiges Rendering: der gesamte UI-Zustand liegt auf dem Server
- Fragen werden beim ersten Start aus einer JSON-Datei in die Datenbank geladen (Seed)

### Verwendete Muster
- MVC (Model–View–Controller)
- Service-Layer-Pattern
- Repository-Pattern (via SQLAlchemy Session)

---

## 🗄️ Datenbank und ORM

Die Applikation verwendet **SQLAlchemy** mit einer **SQLite**-Datenbank.

### Entitäten

| Modell | Beschreibung |
|--------|-------------|
| `User` | Speichert Benutzername und Registrierungszeitpunkt |
| `Question` | Speichert Fragetext, Kapitel und Antwortoptionen |
| `Result` | Speichert Punktzahl, Zeitstempel und Referenz auf den User |

### Beziehungen
- Ein `User` → mehrere `Result`
- Ein `Result` referenziert die zugehörigen `Question`-Objekte der Session

---

## ✅ Projektanforderungen

### 1. Browserbasierte App (NiceGUI)
Die Applikation läuft vollständig im Browser. Benutzer können:
- Sich mit einem Benutzernamen registrieren oder einloggen
- Kapitel und Anzahl Fragen auswählen
- Fragen beantworten und sofortiges Feedback erhalten
- Das Quiz jederzeit abbrechen
- Ergebnisse und das Leaderboard einsehen

**Architektur-Hinweis:** Der Browser ist ein Thin Client. Alle UI-Zustände und Businesslogik laufen serverseitig in der NiceGUI-Applikation.

### 2. Datenvalidierung
Alle Benutzereingaben werden validiert:
- Benutzername muss mindestens 5 Zeichen lang sein, mindestens einen Buchstaben und eine Zahl enthalten, und darf keine Leerzeichen haben
- Benutzername darf nicht bereits vergeben sein
- Kapitelauswahl muss einer gültigen Option entsprechen
- Anzahl Fragen muss 10, 20 oder 30 sein
- Antwort muss einer der angezeigten Optionen entsprechen

### 3. Datenbankverwaltung
Alle Daten werden über das SQLAlchemy ORM gespeichert (kein rohes SQL). Dies umfasst Benutzer, Fragen und Ergebnisse.

---

## ⚙️ Implementierung

### Technologie

| Komponente | Technologie |
|------------|-------------|
| Sprache | Python 3.11+ |
| Frontend | NiceGUI |
| ORM | SQLAlchemy |
| Datenbank | SQLite |
| IDE | Visual Studio Code / GitHub Codespaces |

### 📚 Verwendete Bibliotheken

| Bibliothek | Zweck |
|------------|-------|
| `nicegui` | Browserbasiertes UI-Framework |
| `sqlalchemy` | ORM und Datenbank-Toolkit |
| `sqlite3` | Integrierte Python-Datenbank (via SQLAlchemy) |

---

## 📂 Projektstruktur

```text
flashcards_web/
├── main.py                      # NiceGUI App-Einstiegspunkt
├── views/
│   ├── user_view.py             # Login / Registrierung UI
│   ├── quiz_view.py             # Quiz UI
│   └── leaderboard_view.py      # Leaderboard UI
├── services/
│   ├── user_service.py          # Benutzerverwaltung
│   ├── quiz_service.py          # Quiz-Logik (Auswahl, Mischung, Auswertung)
│   └── result_service.py        # Ergebnisauswertung & Leaderboard
├── models/
│   ├── base.py                  # SQLAlchemy Declarative Base
│   ├── user.py                  # User ORM-Modell
│   ├── question.py              # Question ORM-Modell
│   └── result.py                # Result ORM-Modell
├── questions.json               # Seed-Daten (Fragen aus dem alten CLI-Projekt)
├── requirements.txt             # Python-Abhängigkeiten
└── README.md
```

---

## 🚀 Applikation starten

<<<<<<< HEAD
### 1. Projekt einrichten

Repository klonen:
```bash
git clone https://github.com/REPO-URL-HIER.git
cd flashcards_web
```

Virtuelle Umgebung erstellen und aktivieren:

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\Activate
```

Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

### 2. Starten

```bash
python main.py
```

Die im Terminal angezeigte URL öffnen (Standard: `http://localhost:8080`).

### 3. Verwendung

1. Gültigen Benutzernamen eingeben um sich zu registrieren oder eine bestehende Session fortzuführen
2. Ein oder mehrere Kapitel auswählen (oder alle)
3. Anzahl der Fragen wählen: 10, 20 oder 30
4. Jede Frage beantworten – nach jeder Antwort sofortiges Feedback erhalten
5. Optional: Quiz vorzeitig abbrechen und Zwischenstand einsehen
6. Abschliessende Auswertung mit Punktzahl und Zeitstempel anzeigen
7. Leaderboard anzeigen und eigenen Rang vergleichen

---

## 🧪 Tests

> 🚧 Tests werden im Verlauf der Entwicklung hinzugefügt.

Geplante Testabdeckung:
- **Unit-Tests:** Benutzernamen-Validierung, Punkteberechnung, Kapitel- und Fragenauswahl
- **DB-Tests:** Benutzererstellung, Ergebnisspeicherung, Leaderboard-Abfrage
- **Integrationstests:** Vollständiger Quiz-Ablauf, Abbruch-Ablauf

---

## 👥 Team & Beiträge

| Name | Beitrag |
|------|---------|
| Fabian Vokrraj | 🚧 |
| Albin Tahiri | 🚧 |
| Amir Muliqi | 🚧 |

> Die Beiträge werden anhand der GitHub-Commits überprüft. Alle Teammitglieder müssen direkt Code beitragen.

---

## 🤝 Beitrag

- Dieses Repository als Ausgangspunkt verwenden und in das eigene GitHub-Konto importieren
- Ausschliesslich in der eigenen Kopie arbeiten – keine Änderungen im ursprünglichen Template
- Regelmässige Commits durchführen, um den Fortschritt nachzuverfolgen

---

## 📝 Lizenz

Dieses Projekt wird ausschliesslich zu Bildungszwecken im Rahmen des Moduls *Objektorientierte Programmierung* an der FHNW bereitgestellt.  
[MIT License](LICENSE)
=======
1. Das Projekt „my_project_flashcards“ von GitHub herunterladen und als Projektordner ablegen.
2. In der Python-Konsole mit cd in den Projektordner my_project_flashcards wechseln.
3. Die Datei main.py ausführen.

| Teammitglied   | Beitrag                                 |
| -------------- | --------------------------------------- |
| Fabian Vokrraj | Username, Leaderboard & Flashcards      |
| Albin Tahiri   | Kategorien, Menüführung & Korrektur     |
| Amir Muliqi    | Quiz-Logik, Validierung & Zusammenhänge |

## Beitrag

- Verwende dieses Repository als Ausgangspunkt, indem du es in dein eigenes GitHub-Konto importierst.
- Arbeite ausschließlich in deiner eigenen Kopie – füge keine Änderungen in die ursprüngliche Vorlage ein.
- Führe regelmäßig Commits durch, um deinen Fortschritt nachzuverfolgen.

## Lizenz

Dieses Projekt wird ausschliesslich zu Bildungszwecken im Rahmen des
Moduls Programmierung Grundlagen bereitgestellt. MIT License
>>>>>>> d278fc92bbb7a9fdc180c44b3987b06c30e988cd
