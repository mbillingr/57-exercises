from myio import IO


def main(io):
    try:
        istr = io.input('What is the input string? ')
        response = f'{istr} has {count_chars(istr)} characters'
    except EOFError:
        response = "You must enter something."
    io.println(response)


def count_chars(s: str) -> int:
    return len(s)


if __name__ == '__main__':
    main(IO())
