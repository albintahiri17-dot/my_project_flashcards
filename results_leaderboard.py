import json
import os
from datetime import datetime

LEADERBOARD_FILE = "leaderboard.json"


def load_leaderboard():
    """
    Lädt das Leaderboard aus einer JSON-Datei.
    Rückgabe: Liste von Einträgen oder leere Liste, wenn Datei nicht existiert.

    Format pro Eintrag:
        [username, answered_questions, correct_answers, score_percent, timestamp]
    """
    if not os.path.exists(LEADERBOARD_FILE):
        return []

    with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
        leaderboard = json.load(f)

    return leaderboard


def save_leaderboard(leaderboard):
    """
    Speichert das Leaderboard in die JSON-Datei.

    leaderboard: Liste von Einträgen (siehe load_leaderboard).
    """
    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
        json.dump(leaderboard, f, indent=4)


def compute_score(correct_answers, answered_questions):
    """
    Berechnet die Punktzahl in Prozent.
    Rückgabe: Score als float (0.0 bis 100.0)
    """
    if answered_questions == 0:
        return 0.0

    score = (correct_answers * 100.0) / answered_questions
    return score


def end_session():
    """
    Gibt einen Zeitstempel für das Ende der Session zurück.
    Format: 'YYYY-MM-DD HH:MM:SS'
    """
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return timestamp


def make_summary(username, answered_questions, correct_answers):
    """
    Erstellt einen Ergebnis-Eintrag für das Leaderboard.

    Rückgabe:
        summary = [username, answered, correct, score_percent, timestamp]
    """
    score = compute_score(correct_answers, answered_questions)
    timestamp = end_session()

    summary = [username, answered_questions,
               correct_answers, round(score, 1), timestamp]
    return summary


def display_summary(summary):
    """
    Zeigt die Ergebnisse einer Quiz-Session an.

    summary: Liste [username, answered, correct, score, timestamp]
    """
    username = summary[0]
    answered = summary[1]
    correct = summary[2]
    score = summary[3]
    timestamp = summary[4]

    print("\n=== Auswertung ===")
    print("Benutzer:", username)
    print("Beantwortete Fragen:", answered)
    print("Richtige Antworten:", correct)
    print("Score:", score, "%")
    print("Zeitstempel:", timestamp)


def update_leaderboard(leaderboard, summary):
    """
    Fügt einen neuen Eintrag zum Leaderboard hinzu.

    leaderboard: Liste der bisherigen Einträge
    summary: Eintrag der aktuellen Session

    Rückgabe: aktualisierte Leaderboard-Liste
    """
    leaderboard.append(summary)
    return leaderboard


def show_leaderboard():
    """
    Lädt das Leaderboard, sortiert es nach Score und zeigt die Einträge an.
    Höchste Punktzahl zuerst.
    """
    leaderboard = load_leaderboard()

    if len(leaderboard) == 0:
        print("\nNoch keine Einträge im Leaderboard vorhanden.")
        return

    # Sortieren nach Score (Index 3), absteigend
    sorted_leaderboard = sorted(
        leaderboard, key=lambda entry: entry[3], reverse=True)

    print("\n=== Leaderboard ===")
    print("Rang | Benutzer       | Score  | Richtig/Fragen | Zeitpunkt")
    print("--------------------------------------------------------------")

    rank = 1
    for entry in sorted_leaderboard:
        username = entry[0]
        answered = entry[1]
        correct = entry[2]
        score = entry[3]
        timestamp = entry[4]

        print(
            str(rank).ljust(4), "|",
            username.ljust(14), "|",
            (str(score) + "%").ljust(6), "|",
            (str(correct) + "/" + str(answered)).ljust(15), "|",
            timestamp
        )
        rank = rank + 1
