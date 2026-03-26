#!/usr/bin/env python3
"""Игра "Арифметическая прогрессия"."""

from VD_games.games.progression import generate_question
from VD_games.games.engine import run_game


def main():
    """Запускает игру."""
    game_description = "What number is missing in the progression?"
    run_game(generate_question, game_description)


if __name__ == "__main__":
    main()
