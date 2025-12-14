from username_setup import (
    prompt_username,
    is_username_taken,
    validate_username,
    register_user,
)

from quiz_setup import (
    load_questions_from_json,
    select_chapters,
    select_question_count,
)

from quiz_run import (
    shuffle_questions,
    get_next_question,
    present_question,
    get_valid_answer,
    check_answer,
    give_feedback,
    handle_quitting,
)

from results_leaderboard import (
    load_leaderboard,
    save_leaderboard,
    make_summary,
    display_summary,
    update_leaderboard,
    show_leaderboard,
)


def main():
    print("=== Willkommen zum Flashcards-Quiz ===")

    leaderboard = load_leaderboard()

    usernames = []
    for entry in leaderboard:
        if isinstance(entry, dict) and "username" in entry:
            usernames.append(entry["username"])

    while True:
        username = prompt_username()

        if not validate_username(username):
            continue

        if is_username_taken(usernames, username):
            print("👤 Willkommen zurück,", username)
            break
        else:
            print("✅ Neuer Benutzer registriert:", username)
            leaderboard = register_user(leaderboard, username)
            save_leaderboard(leaderboard)
            usernames.append(username)
            break

    questions_by_chapter = load_questions_from_json("questions.json")

    # Kapitel-Liste aus dem JSON erzeugen
    available_chapters = list(questions_by_chapter.keys())
    available_chapters.sort()

    # 3)

    selected_chapters = select_chapters(available_chapters)

    # Ausgewählte Fragen in eine flache Liste umwandeln
    selected_questions = []
    for chapter in selected_chapters:
        question_list = questions_by_chapter.get(chapter, [])
        for q in question_list:
            question_entry = {
                "chapter": chapter,
                "question": q["question"],
                "options": q["options"],
                "answer": q["answer"],
            }
            selected_questions.append(question_entry)

    if len(selected_questions) == 0:
        print("Es wurden keine Fragen gefunden. Programm wird beendet.")
        return

    max_questions = len(selected_questions)
    num_to_ask = select_question_count(max_questions)

    # Fragen mischen und auf gewünschte Anzahl kürzen
    selected_questions = shuffle_questions(selected_questions)
    selected_questions = selected_questions[:num_to_ask]

    # 4) DURCHFÜHRUNG DES QUIZ

    index = 0
    num_correct = 0
    asked = 0
    aborted = False

    while True:
        question, index = get_next_question(selected_questions, index)
        if question is None:
            break

        asked += 1
        present_question(question, asked, len(selected_questions))

        user_answer = get_valid_answer(len(question["options"]))

        if user_answer == "q":
            aborted = True
            break

        is_correct = check_answer(question, user_answer)
        give_feedback(is_correct)

        if is_correct:
            num_correct += 1

    get_valid_answer,

    # 5) ERGEBNIS & LEADERBOARD

    summary = make_summary(username, num_correct, asked, aborted)
    display_summary(summary)

    leaderboard = update_leaderboard(leaderboard, summary)
    save_leaderboard(leaderboard)

    show_leaderboard(leaderboard)


if __name__ == "__main__":
    main()
