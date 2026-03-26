"""Модуль для приветствия пользователя."""

from VD_games.lib.prompt import string


def welcome_user():
    """Приветствует пользователя и запрашивает имя."""
    print("Welcome to the VD Games!")
    
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    return name
