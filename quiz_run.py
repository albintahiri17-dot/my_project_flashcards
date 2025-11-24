# quiz_run.py
# Durchführung des Quiz: Fragen mischen, anzeigen, prüfen, Abbruch ermöglichen

import random


def shuffle_questions(questions):
    """
    Mischt die Liste der Fragen zufällig.
    questions: Liste von Frage-Dictionaries mit Schlüsseln:
      - "chapter"
      - "question"
      - "options"
      - "answer"
    """
    random.shuffle(questions)
    return questions


def get_next_question(questions, index):
    """
    Gibt die nächste Frage aus der Liste zurück.

    questions: Liste der Fragen
    index: aktuelle Position (int)

    Rückgabe:
      - question: nächste Frage (Dictionary) oder None, wenn keine mehr
      - new_index: index + 1 oder unverändert, wenn keine mehr
    """
    if index >= len(questions):
        return None, index

    question = questions[index]
    new_index = index + 1
    return question, new_index


def present_question(question, question_number, total_questions):
    """
    Zeigt eine Frage mit Antwortoptionen an.
    question: Dictionary mit 'chapter', 'question', 'options'
    """
    print()
    print("Kapitel:", question["chapter"])
    print("Frage", question_number, "von", total_questions)
    print(question["question"])

    for option in question["options"]:
        print(option)

    print()
    print("Gib die Nummer deiner Antwort ein oder 'q' zum Abbrechen.")


def check_answer(question, answer_number):
    """
    Prüft, ob die gegebene Antwortnummer korrekt ist.
    question: Dictionary mit 'answer' (int)
    answer_number: vom Benutzer eingegebene Zahl (int)

    Rückgabe: True (richtig) oder False (falsch)
    """
    correct_number = question["answer"]
    return answer_number == correct_number


def give_feedback(is_correct):
    """Gibt sofortiges Feedback (richtig/falsch)."""
    if is_correct:
        print("✅ Richtig!")
    else:
        print("❌ Falsch.")


def handle_quitting(user_input):
    """
    Prüft, ob der Benutzer das Quiz abbrechen möchte.
    user_input: Eingabe-String

    Rückgabe: True, wenn abgebrochen werden soll, sonst False.
    """
    if user_input.lower() == "q":
        print("Das Quiz wurde abgebrochen.")
        return True
    return False
