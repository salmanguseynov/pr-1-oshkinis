#!/usr/bin/env python3
"""Игра "Проверка на чётность"."""

import random

from VD_games.cli import welcome_user


def is_even(number):
    """Проверяет, является ли число чётным."""
    return number % 2 == 0


def run_game():
    """Запускает игру."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    rounds_to_win = 3

    while correct_answers < rounds_to_win:
        number = random.randint(1, 100)
        print(f"\nQuestion: {number}")
        user_answer = input("Your answer: ").strip().lower()

        correct_answer = "yes" if is_even(number) else "no"

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            # Разбиваем длинную строку на две
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    """Главная функция."""
    run_game()


if __name__ == "__main__":
    main()
