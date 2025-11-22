
# main.py
# Startpunkt der gesamten Applikation: Benutzer anmelden, Quiz vorbereiten, Quiz durchführen, Ergebnisse speichern

# main.py
# Startpunkt der gesamten Applikation

# main.py
# Startpunkt der gesamten Applikation

from username_setup import (
    prompt_username,
    is_username_taken,
    validate_username,
    register_user
)

from quiz_setup import (
    select_chapters,
    select_question_count,
    load_questions_from_json
)

from quiz_run import (
    shuffle_questions,
    get_next_question,
    present_question,
    check_answer,
    give_feedback,
    handle_quitting
)

from results_leaderboard import (
    make_summary,
    display_summary,
    load_leaderboard,
    save_leaderboard,
    update_leaderboard,
    show_leaderboard
)


def main():
    print("=== Willkommen zum Flashcards-Quiz ===")

    # -------------------------------
    # 1) BENUTZERVERWALTUNG
    # -------------------------------
    leaderboard = load_leaderboard()

    username = prompt_username()

    # Wiederholen, bis Benutzername gültig ist
    while not validate_username(username):
        username = prompt_username()

    # Prüfen, ob der Name existiert – falls ja → weiter
    # falls nein → registrieren
    if is_username_taken(leaderboard, username):
        print("👤 Willkommen zurück,", username)
    else:
        print("Neuer Benutzer:", username)
        leaderboard = register_user(leaderboard, username)
        save_leaderboard(leaderboard)

    # -------------------------------
    # 2) FRAGEN LADEN
    # -------------------------------
    questions = load_questions_from_json("questions.json")

    # verfügbare Kapitel sammeln
    available_chapters = []
    for q in questions:
        chapter = q[0]
        if chapter not in available_chapters:
            available_chapters.append(chapter)

    available_chapters.sort()

    # -------------------------------
    # 3) QUIZ-SETUP
    # -------------------------------
    selected_chapters = select_chapters(available_chapters)

    # Fragen nach Kapiteln filtern
    filtered_questions = []
    for q in questions:
        if q[0] in selected_chapters:
            filtered_questions.append(q)

    if len(filtered_questions) == 0:
        print("Keine Fragen in diesen Kapiteln vorhanden.")
        return

    # Anzahl der Fragen bestimmen
    question_count = select_question_count(len(filtered_questions))

    # Fragen mischen
    filtered_questions = shuffle_questions(filtered_questions)

    # -------------------------------
    # 4) DURCHFÜHRUNG
    # -------------------------------
    answered = 0
    correct = 0
    index = 0

    while answered < question_count:
        question, index = get_next_question(filtered_questions, index)

        if question is None:
            break

        choice, quit_flag = present_question(
            question, answered + 1, question_count)

        if quit_flag:
            handle_quitting()
            break

        if choice is not None:
            result = check_answer(question, choice)
            give_feedback(result)

            answered = answered + 1
            if result:
                correct = correct + 1

    # -------------------------------
    # 5) ERGEBNISSE
    # -------------------------------
    summary = make_summary(username, answered, correct)
    display_summary(summary)

    leaderboard = load_leaderboard()
    leaderboard = update_leaderboard(leaderboard, summary)
    save_leaderboard(leaderboard)

    # Leaderboard anzeigen
    print("\nMöchtest du das Leaderboard sehen? (j/n)")
    choice = input().lower()

    if choice == "j":
        show_leaderboard()

    print("\n=== Programm beendet. Danke fürs Spielen! ===")


if __name__ == "__main__":
    main()
