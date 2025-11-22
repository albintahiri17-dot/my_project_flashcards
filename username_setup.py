# username_setup.py
import json

# Datei, in der Benutzerdaten gespeichert werden
DATA_FILE = "leaderboard.json"


def prompt_username():
    """Fragt den Benutzer nach einem Benutzernamen."""
    username = input("Bitte gib deinen Benutzernamen ein: ").strip()
    return username


def is_username_taken(usernames, username):
    """Prüft, ob ein Benutzername bereits existiert."""
    while True:
        name_exists = False

        for name in usernames:
            if name == username:
                name_exists = True
                break

        if not name_exists:
            return username  # Name ist frei

        print("❗ Dieser Benutzername ist bereits vergeben. Bitte gib einen anderen ein.")
        username = input("Bitte neuen Benutzernamen eingeben: ").strip()


def validate_username(username):
    """Überprüft, ob der eingegebene Benutzername gültig ist."""
    if username == "":
        print("⚠️ Benutzername darf nicht leer sein.")
        return False
    return True


def register_user(leaderboard, username):
    """Fügt einen neuen Benutzer in die Leaderboard-Daten ein."""
    leaderboard.append([username, 0, 0, 0, ""])
    return leaderboard
