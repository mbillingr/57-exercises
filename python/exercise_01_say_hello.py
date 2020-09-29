from python.myio import IO


def main(io):
    name = io.input('What is your name? ')
    response = f'Hello, {name}, nice to meet you!'
    io.println(response)


if __name__ == '__main__':
    main(IO())
