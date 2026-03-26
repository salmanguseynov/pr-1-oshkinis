#!/usr/bin/env python3
"""Игра "Наибольший общий делитель (НОД)"."""

from VD_games.games.gcd import generate_question
from VD_games.games.engine import run_game


def main():
    """Запускает игру."""
    game_description = "Find the greatest common divisor of given numbers."
    run_game(generate_question, game_description)


if __name__ == "__main__":
    main()
