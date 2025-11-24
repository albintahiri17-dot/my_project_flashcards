
import json
from results_leaderboard import load_leaderboard, save_leaderboard


def prompt_username():
    """Fragt den Benutzer nach einem Benutzernamen."""
    username = input(
        "Bitte gib deinen Benutzernamen ein.\n"
        "Er sollte aus Buchstaben und mindestens einer Ziffer bestehen\n"
        "und mindestens 5 Zeichen lang sein: "
    )
    return username.strip()


def validate_username(username):
    """
    Prüft, ob der Benutzername die grundlegenden Regeln erfüllt:
    - nicht leer
    - keine Leerzeichen
    - mindestens 5 Zeichen
    - mindestens ein Buchstabe und mindestens eine Ziffer
    """
    if username == "":
        print("⚠️  Benutzername darf nicht leer sein.")
        return False

    if " " in username:
        print("⚠️  Benutzername darf keine Leerzeichen enthalten.")
        return False

    if len(username) < 5:
        print("⚠️  Benutzername muss mindestens 5 Zeichen lang sein.")
        return False

    has_letter = False
    has_digit = False
    for ch in username:
        if ch.isalpha():
            has_letter = True
        if ch.isdigit():
            has_digit = True

    if not has_letter or not has_digit:
        print(
            "⚠️  Benutzername muss mindestens einen Buchstaben und eine Ziffer enthalten.")
        return False

    return True


def is_username_taken(usernames, username):
    """
    Prüft, ob der angegebene Benutzername bereits in der übergebenen Liste vorkommt.
    usernames: Liste von Strings
    username: zu prüfender Name
    """
    for name in usernames:
        if name == username:
            return True
    return False


def register_user(leaderboard, username):
    """
    Registriert einen neuen Benutzer im Leaderboard.
    Falls die Struktur noch nicht existiert, wird ein neuer Eintrag mit Score 0 angelegt.
    """
    new_entry = {
        "username": username,
        "score": 0,
        "total": 0,
        "date": ""
    }
    leaderboard.append(new_entry)
    save_leaderboard(leaderboard)
    return leaderboard
