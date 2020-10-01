from python.myio import IO
from python.currency import Dollar


TAX_RATES_PERCENT = {'WI': 5.5}


def get_inputs(io: IO):
    amount = io.input_number('What is the order amount? ')
    state = io.input('What is the state? ')

    state = state.upper()

    return amount, state


def format_output(total, subtotal=None, tax=None):
    s = ''

    if subtotal is not None:
        s += f'The subtotal is {subtotal}.\n'

    if tax is not None:
        s += f'The tax is {tax}.\n'

    s += f'The total is {total}.'

    return s


def compute_tax(amount, state):
    subtotal = None
    tax = None
    total = amount

    if state == 'WI':
        rate = TAX_RATES_PERCENT[state] / 100
        subtotal = amount
        tax = amount * rate
        total += tax

    return total, subtotal, tax


def main(io: IO):
    amount, state = get_inputs(io)

    amount = Dollar(amount)

    io.println(format_output(*compute_tax(amount, state)))


if __name__ == '__main__':
    main(IO())
