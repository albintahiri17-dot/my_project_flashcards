# results_leaderboard.py
# Bereich: ERGEBNISSE & LEADERBOARD

import json
import os
from datetime import datetime

DATA_FILE = "leaderboard.json"


def load_leaderboard():
    """
    Lädt das Leaderboard aus der JSON-Datei.
    Falls die Datei nicht existiert oder leer/ungültig ist, wird eine leere Liste zurückgegeben.
    """
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = f.read().strip()
            if data == "":
                return []
            return json.loads(data)
    except (json.JSONDecodeError, OSError):
        # Falls die Datei beschädigt ist, mit leerer Liste neu anfangen
        return []


def save_leaderboard(leaderboard):
    """Speichert das Leaderboard in der JSON-Datei."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(leaderboard, f, indent=2, ensure_ascii=False)


def make_summary(username, score, total, aborted):
    """
    Erstellt eine Zusammenfassung der aktuellen Session.
    score: Anzahl richtig beantworteter Fragen
    total: Anzahl gestellter Fragen
    aborted: True, falls abgebrochen wurde
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    summary = {
        "username": username,
        "score": score,
        "total": total,
        "date": now,
        "aborted": aborted
    }
    return summary


def display_summary(summary):
    """Zeigt die Zusammenfassung der aktuellen Session an."""
    print()
    print("=== AUSWERTUNG ===")
    print("Benutzer:", summary["username"])
    print("Richtige Antworten:", summary["score"], "von", summary["total"])

    if summary["total"] > 0:
        percentage = summary["score"] / summary["total"] * 100
        print("Prozent:", f"{percentage:.1f}%")
    else:
        print("Keine Fragen beantwortet.")

    if summary["aborted"]:
        print("Hinweis: Quiz wurde vorzeitig abgebrochen.")

    print("Datum:", summary["date"])
    print("===================")


def update_leaderboard(leaderboard, summary):
    """
    Aktualisiert das Leaderboard mit der aktuellen Session.
    - Wenn der Benutzer bereits existiert, wird der Eintrag aktualisiert,
      falls der neue Score besser ist.
    - Andernfalls wird ein neuer Eintrag hinzugefügt.
    """
    username = summary["username"]
    score = summary["score"]
    total = summary["total"]
    date = summary["date"]

    found = False
    for entry in leaderboard:
        if isinstance(entry, dict) and entry.get("username") == username:
            found = True
            # Falls neuer Score besser ist, aktualisieren
            if score > entry.get("score", 0):
                entry["score"] = score
                entry["total"] = total
                entry["date"] = date
            break

    if not found:
        leaderboard.append({
            "username": username,
            "score": score,
            "total": total,
            "date": date
        })

    return leaderboard


def show_leaderboard(leaderboard):
    """Zeigt das Leaderboard sortiert nach Score an."""
    print()
    print("=== LEADERBOARD ===")

    # Nur gültige Einträge berücksichtigen
    valid_entries = []
    for entry in leaderboard:
        if isinstance(entry, dict) and "username" in entry:
            valid_entries.append(entry)

    # Nach Score absteigend sortieren
    valid_entries.sort(key=lambda e: e.get("score", 0), reverse=True)

    if len(valid_entries) == 0:
        print("Noch keine Einträge vorhanden.")
        return

    print(f"{'Platz':<6} {'Name':<15} {'Score':<7} {'Total':<7} {'Datum':<19}")
    print("-" * 60)

    rank = 1
    for entry in valid_entries:
        print(
            f"{rank:<6} {entry['username']:<15} "
            f"{entry.get('score', 0):<7} {entry.get('total', 0):<7} {entry.get('date', ''):<19}"
        )
        rank += 1

    print("===================")
