import json


def load_questions_from_json(filename="questions.json"):

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def select_chapters(available_chapters):
    """
    Lässt den Benutzer Kapitel auswählen.

    Erlaubt:
    - 'all' für alle Kapitel
    - eine Zahl zwischen 1 und Anzahl Kapitel

    Wiederholt die Eingabe so lange, bis sie gültig ist.
    """
    print("=== Quiz-Setup: Kapitel auswählen ===")
    print("Verfügbare Kapitel:")

    for index, chapter in enumerate(available_chapters, start=1):
        print(index, "-", chapter)

    while True:
        print("Gib eine Kapitelnummer ein (oder 'all' für alle Kapitel).")
        user_input = input("Deine Auswahl: ").strip().lower()

        if user_input == "all":
            return available_chapters

        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= len(available_chapters):
                return [available_chapters[choice - 1]]

        print(
            "❗ Ungültige Eingabe. Bitte gib eine Zahl zwischen 1 und "
            f"{len(available_chapters)} ein oder 'all'."
        )


def select_question_count(max_questions):

    print("\n=== Anzahl der Fragen auswählen ===")
    print("1) 10 Fragen")
    print("2) 20 Fragen")
    print("3) 30 Fragen")

    valid_choices = {"1": 10, "2": 20, "3": 30}

    while True:
        user_input = input("Bitte wähle 1, 2 oder 3: ").strip()

        if user_input not in valid_choices:
            print("❗ Ungültige Eingabe. Bitte 1, 2 oder 3 eingeben.")
            continue

        chosen_amount = valid_choices[user_input]

        if chosen_amount > max_questions:
            print(f"⚠️  Es sind nur {max_questions} Fragen verfügbar. "
                  f"Es werden {max_questions} Fragen gestellt.")
            return max_questions

        return chosen_amount
