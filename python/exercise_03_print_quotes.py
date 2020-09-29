from python.myio import IO


def main(io):
    quote = io.input('What is the quote? ')
    author = io.input('Who said it? ')

    response = construct_quote(author, quote)

    io.println(response)


def construct_quote(author, quote):
    return author + ' says, "' + quote + '"'


if __name__ == '__main__':
    main(IO())
