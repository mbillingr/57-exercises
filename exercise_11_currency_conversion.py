from numbers import Real
from myio import IO
import math
from typing import List, Tuple
from currency import Currency, Euro, Dollar


def main(io: IO):
    euros = io.input_number(f'How many euros are you exchanging? ')
    rate = io.input_number(f'What is the exchange rate? ')

    euros = Euro(euros)
    dollars = Dollar.convert_from(euros, rate)

    io.println(f"{euros} at an exchange rate of {rate} is {dollars}.")


if __name__ == '__main__':
    main(IO())
