#!/usr/bin/env python3
"""Игра "Калькулятор"."""

from VD_games.games.calc import generate_question
from VD_games.games.engine import run_game


def main():
    """Запускает игру."""
    game_description = "What is the result of the expression?"
    run_game(generate_question, game_description)


if __name__ == "__main__":
    main()
