from myio import IO
from numbers import Number


def main(io):
    a = io.input('What is the first number? ')
    b = io.input('What is the second number? ')

    a = string_to_number(a)
    b = string_to_number(b)

    io.println(f'{a} + {b} = {a + b}\n'
               f'{a} - {b} = {a - b}\n'
               f'{a} * {b} = {a * b}\n'
               f'{a} / {b} = {a // b}')


def string_to_number(s: str) -> Number:
    try:
        return int(s)
    except ValueError:
        pass

    return float(s)


if __name__ == '__main__':
    main(IO())
