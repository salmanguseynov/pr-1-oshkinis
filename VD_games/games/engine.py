"""Движок для запуска игр."""

from VD_games.cli import welcome_user


def run_game(game_logic, game_description):
    """
    Запускает игру с заданной логикой.

    Args:
        game_logic: функция, которая генерирует вопрос и правильный ответ
        game_description: описание игры
    """
    name = welcome_user()
    print(game_description)

    correct_answers = 0
    rounds_to_win = 3

    while correct_answers < rounds_to_win:
        question, correct_answer = game_logic()
        print(f"\nQuestion: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
