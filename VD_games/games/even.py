"""Игра "Проверка на чётность"."""

import random


def is_even(number):
    """Проверяет, является ли число чётным."""
    return number % 2 == 0


def generate_question():
    """Генерирует случайное число для проверки чётности."""
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer
