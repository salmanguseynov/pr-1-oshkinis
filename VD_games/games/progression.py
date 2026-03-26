"""Игра "Арифметическая прогрессия"."""

import random


def generate_progression():
    """Генерирует арифметическую прогрессию с пропущенным элементом."""
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    
    # Генерируем прогрессию
    progression = [start + i * step for i in range(length)]
    
    # Выбираем случайную позицию для пропуска
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    
    # Создаем строку с пропуском
    progression_str = []
    for i, num in enumerate(progression):
        if i == hidden_index:
            progression_str.append("..")
        else:
            progression_str.append(str(num))
    
    question = " ".join(progression_str)
    return question, correct_answer


def generate_question():
    """Генерирует вопрос для игры."""
    return generate_progression()
