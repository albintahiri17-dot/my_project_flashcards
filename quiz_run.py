# 03_Durchführung.py
# Durchführung des Quiz: Fragen mischen, anzeigen, prüfen, Abbruch ermöglichen

import random


def shuffle_questions(questions):
    """
    Mischt die Liste der Fragen zufällig.

    questions: Liste von Tupeln
        (chapter, question_text, options_list, correct_number)

    Rückgabe: die gleiche Liste in zufälliger Reihenfolge.
    """
    random.shuffle(questions)
    return questions


def get_next_question(questions, index):
    """
    Gibt die nächste Frage aus der Liste zurück.

    questions: Liste der Fragen
    index: aktuelle Position (int)

    Rückgabe:
        - question: nächste Frage oder None, wenn keine mehr vorhanden
        - new_index: index + 1
    """
    if index >= len(questions):
        return None, index
    else:
        question = questions[index]
        new_index = index + 1
        return question, new_index


def allow_quitting(user_input):
    """
    Prüft, ob der Benutzer das Quiz abbrechen möchte.
    Der Benutzer kann mit 'q' oder 'Q' abbrechen.
    """
    if user_input == "q" or user_input == "Q":
        return True
    else:
        return False


def handle_quitting():
    """Wird aufgerufen, wenn der Benutzer das Quiz abbricht."""
    print("Du hast das Quiz abgebrochen.")


def present_question(question, number, total):
    """
    Zeigt eine Frage mit Antwortmöglichkeiten an und liest die Eingabe ein.

    question: Tupel (chapter, text, options_list, correct_number)
    number: laufende Nummer der Frage (1..total)
    total: Gesamtanzahl der Fragen im Quiz

    Rückgabe:
        - user_choice: gewählte Nummer (1–4) oder None bei Abbruch
        - quit_flag: True, wenn Benutzer abgebrochen hat, sonst False
    """
    chapter = question[0]
    text = question[1]
    options = question[2]

    print()
    print("Kapitel:", chapter)
    print("Frage", number, "von", total)
    print(text)

    # Antwortmöglichkeiten anzeigen (1–4)
    for i in range(len(options)):
        print(i + 1, ")", options[i])

    print("Gib die Nummer deiner Antwort ein oder 'q' zum Abbrechen.")

    while True:
        user_input = input("Deine Eingabe: ")
        user_input = user_input.strip()

        # Abbruch prüfen
        if allow_quitting(user_input):
            return None, True

        # Zahl prüfen
        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= len(options):
                return choice, False

        print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und",
              len(options), "oder 'q' eingeben.")


def check_answer(question, user_choice):
    """
    Prüft, ob die Antwort richtig ist.

    question: Tupel (chapter, text, options_list, correct_number)
    user_choice: gewählte Antwortnummer (1–4)

    Rückgabe: True (richtig) oder False (falsch).
    """
    correct_number = question[3]
    if user_choice == correct_number:
        return True
    else:
        return False


def give_feedback(is_correct):
    """
    Gibt sofort Feedback zur Antwort.
    """
    if is_correct:
        print("✅ Richtig!")
    else:
        print("❌ Falsch.")
