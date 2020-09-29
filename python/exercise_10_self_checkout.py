from python.myio import IO
from typing import List, Tuple
from python.currency import Currency, Euro


TAX_RATE = 0.055


def total_price(basket: List[Tuple[int, Currency]]) -> Currency:
    item_prices = map(lambda item: item[0] * item[1], basket)
    return sum(item_prices, Euro(0))


def compute_tax(price: Currency, rate: float) -> Currency:
    value = price.as_universal_value()
    tax = value * rate
    return type(price).from_universal_value(tax)


def main(io: IO):
    inputs = []
    item_number = 0
    while True:
        item_number += 1
        quantity = io.input_number(f'Enter the quantity of item {item_number}: ')
        if quantity == 0:
            break
        price = io.input(f'Enter the price of item {item_number}: ')
        inputs.append((quantity, price))

    basket = map(lambda item: (item[0], Euro(item[1])), inputs)
    subtotal = total_price(basket)
    tax = compute_tax(subtotal, TAX_RATE)
    total = subtotal + tax

    io.println(f"Subtotal: {subtotal}")
    io.println(f"Tax: {tax}")
    io.println(f"Total: {total}")


if __name__ == '__main__':
    main(IO())
