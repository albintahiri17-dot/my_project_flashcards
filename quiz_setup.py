import json


def validate_chapter(user_input, available_chapters):
    """
    Prüft, ob die eingegebene Kapitelnummer gültig ist.

    user_input: Eingabe-String vom Benutzer
    available_chapters: Liste mit verfügbaren Kapitelnummern (z.B. [1, 2, 3])

    Rückgabe:
        - Kapitelnummer (int), wenn gültig
        - None, wenn die Eingabe ungültig ist
    """
    # Prüfen, ob überhaupt eine Zahl eingegeben wurde
    if not user_input.isdigit():
        return None

    chapter_number = int(user_input)

    # Prüfen, ob die Zahl in der Liste der verfügbaren Kapitel vorkommt
    for c in available_chapters:
        if c == chapter_number:
            return chapter_number

    return None


def select_chapters(available_chapters):
    """
    Lässt den Benutzer Kapitel auswählen.

    available_chapters: Liste der vorhandenen Kapitel (z.B. [1, 2, 3, 4])

    Der Benutzer kann:
      - eine einzelne Kapitelnummer eingeben
      - oder 'all' schreiben, um alle Kapitel zu verwenden

    Rückgabe: Liste der ausgewählten Kapitel (z.B. [1, 2])
    """
    print("=== Quiz-Setup: Kapitel auswählen ===")
    print("Verfügbare Kapitel:")
    for c in available_chapters:
        print("Kapitel", c)

    choice = input(
        "Gib eine Kapitelnummer ein (oder 'all' für alle Kapitel): ")
    choice = choice.strip().lower()

    # alle Kapitel verwenden
    if choice == "all":
        return available_chapters

    # einzelnes Kapitel prüfen
    chapter = validate_chapter(choice, available_chapters)

    if chapter is None:
        print("Ungültige Eingabe. Es werden alle Kapitel verwendet.")
        return available_chapters
    else:
        # Immer eine Liste zurückgeben
        return [chapter]


def select_question_count(max_questions):
    """
    Fragt den Benutzer, wie viele Fragen er beantworten möchte.

    max_questions: maximale Anzahl vorhandener Fragen

    Rückgabe: Anzahl Fragen (int, zwischen 1 und max_questions)
    """
    print("Für deine Auswahl stehen", max_questions, "Fragen zur Verfügung.")

    while True:
        user_input = input("Wie viele Fragen möchtest du beantworten? ")
        user_input = user_input.strip()

        if not user_input.isdigit():
            print("Bitte gib eine Zahl ein.")
            continue

        count = int(user_input)

        if count < 1 or count > max_questions:
            print("Bitte eine Zahl zwischen 1 und", max_questions, "eingeben.")
        else:
            return count


def load_questions_from_json(filename):
    """Lädt Fragen aus einer JSON-Datei."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
