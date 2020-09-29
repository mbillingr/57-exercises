from typing import Tuple

from python.myio import IO
from python.pluralize import pluralize

SQUARE_METERS_PER_SQUARE_FOOT = 0.09290304


def divide_pizzas(n_people: int, n_pizzas: int, n_pieces: int) -> Tuple[int, int]:
    if n_people == 0:
        raise ValueError("No people eat no pizza")
    total_pieces = n_pizzas * n_pieces
    pieces_per_person = total_pieces // n_people
    leftover = total_pieces % n_people
    return pieces_per_person, leftover


def count(n: int, noun: str) -> str:
    return f"{n} {pluralize(n, noun)}"


def main(io: IO):
    n_people = io.input_number('How many people? ')
    n_pizzas = io.input_number('How many pizzas do you have? ')
    n_pieces = io.input_number('How many pieces per pizza? ')

    pieces_per_person, leftover = divide_pizzas(n_people, n_pizzas, n_pieces)

    io.println(f"{count(n_people, 'person')} with {count(n_pizzas, 'pizza')}")
    io.println(f"Each person gets {count(pieces_per_person, 'piece')} of pizza.")
    io.println(f"There {pluralize(leftover, 'is')} {leftover} leftover {pluralize(leftover, 'piece')}.")


if __name__ == '__main__':
    main(IO())
