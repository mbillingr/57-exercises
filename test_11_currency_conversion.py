from myio import IO
from myio_testing import InputMock, OutputSpy
from exercise_11_currency_conversion import main
import currency


def test_zero_euro_are_zero_dollars():
    eur = currency.Euro(euros=0)

    usd = currency.Dollar.convert_from(eur, 0.5)

    assert usd == currency.Dollar(0)


def test_two_euros_are_two_dollars_if_rate_is_one():
    eur = currency.Euro(euros=2)

    usd = currency.Dollar.convert_from(eur, 1)

    assert usd == currency.Dollar(2)


def test_two_euros_are_four_dollars_if_rate_is_two():
    eur = currency.Euro(euros=2)

    usd = currency.Dollar.convert_from(eur, 2)

    assert usd == currency.Dollar(4)


def test_conversion_rounds_up_cents():
    eur = currency.Euro(euros=1)

    usd = currency.Dollar.convert_from(eur, 1.001)

    assert usd == currency.Dollar('1.01')


def test_full_program_three_items():
    out = OutputSpy()
    inp = InputMock('81', '1.3751')

    main(IO(output=out, input=inp))
    assert out.buffers[2:] == ['€81.00 at an exchange rate of 1.3751 is $111.39.\n']
