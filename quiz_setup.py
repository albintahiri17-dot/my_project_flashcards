
import json


def load_questions_from_json(filename="questions.json"):
    """
    Lädt Fragen aus einer JSON-Datei.
    Erwartetes Format (Beispiel):
    {
      "Kapitel 1 – ...": [
         { "question": "...", "options": ["1)...","2)..."], "answer": 2 },
         ...
      ],
      "Kapitel 2 – ...": [ ... ]
    }
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def select_chapters(available_chapters):
    """
    Lässt den Benutzer Kapitel auswählen.
    - available_chapters: Liste der Kapitelnamen (Strings)

    Rückgabe: Liste der ausgewählten Kapitel (Strings)
    """
    print("=== Quiz-Setup: Kapitel auswählen ===")
    print("Verfügbare Kapitel:")

    for index, chapter in enumerate(available_chapters, start=1):
        print(index, "-", chapter)

    print("Gib eine Kapitelnummer ein (oder 'all' für alle Kapitel).")

    user_input = input("Deine Auswahl: ").strip().lower()

    if user_input == "all":
        return available_chapters

    if user_input.isdigit():
        choice = int(user_input)
        if choice >= 1 and choice <= len(available_chapters):
            return [available_chapters[choice - 1]]

    print("Ungültige Eingabe. Es werden alle Kapitel verwendet.")
    return available_chapters


def select_question_count(max_questions):
    """
    Fragt den Benutzer, wie viele Fragen er beantworten möchte.
    max_questions: maximale Anzahl verfügbarer Fragen

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
