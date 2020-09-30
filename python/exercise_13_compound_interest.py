from python.myio import IO
from python.currency import Euro


def get_inputs(io):
    principal = io.input_number(f'Enter the principal: ')
    interest_rate_percent = io.input_number(f'Enter the rate of interest: ')
    years = io.input_number(f'Enter the number of years: ')
    compounds = io.input_number(f'How often is the interest compounded per year? ')
    return principal, interest_rate_percent, years, compounds


def format_output(principal=1, rate_percent=2, years=3, compounds=4, final_value=5):
    return (f"{principal} "
            f"invested at {rate_percent}% "
            f"for {years} years "
            f"compounded {compounds} times per year "
            f"is {final_value}.")


def compute_compound_interest(principal, rate, years, compounds):
    final_value = principal * (1 + rate / compounds) ** (years * compounds)
    return final_value


def main(io: IO):
    principal, interest_rate_percent, years, compounds = get_inputs(io)

    interest_rate = interest_rate_percent / 100
    starting_value = Euro(principal)

    final_value = compute_compound_interest(starting_value, interest_rate, years, compounds)

    io.println(format_output(starting_value, interest_rate_percent, years, compounds, final_value))


if __name__ == '__main__':
    main(IO())
