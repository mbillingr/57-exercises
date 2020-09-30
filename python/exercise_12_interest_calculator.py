from python.myio import IO
from python.currency import Euro


def main(io: IO):
    principal = io.input_number(f'Enter the principal: ')
    interest_rate = io.input_number(f'Enter the rate of interest: ')
    years = io.input_number(f'Enter the number of years: ')

    starting_value = Euro(principal)
    final_value = starting_value * (1 + years * interest_rate / 100)

    io.println(f"After {years} years at {interest_rate}%, the investment will be worth {final_value}.")


if __name__ == '__main__':
    main(IO())
