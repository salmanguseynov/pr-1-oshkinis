"""Модуль для приветствия пользователя."""


def welcome_user():
    """Приветствует пользователя и запрашивает имя."""
    print("VD-even")
    print("Welcome to the VD-games!")

    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name
