from python.myio import IO


def get_inputs(io: IO) -> str:
    pw = io.input('What is the password? ')
    return pw


def validate(pw: str):
    return pw == 'abc$123'


def main(io: IO):
    pw = get_inputs(io)

    if validate(pw):
        io.println("Welcome!")
    else:
        io.println("I don't know you.")


if __name__ == '__main__':
    main(IO())
