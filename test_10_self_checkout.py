import pytest
from myio import IO
from myio_testing import InputMock, OutputSpy
from exercise_10_self_checkout import total_price, compute_tax, main
import currency


def test_zero_euro_are_zero_cents():
    eur = currency.Euro(euros=0)
    cnt = currency.Euro(cents=0)

    assert eur == cnt


def test_different_euro_amount_not_equal():
    eur1 = currency.Euro(1)
    eur2 = currency.Euro(2)

    assert eur1 != eur2


def test_one_euro_are_hundred_cents():
    eur = currency.Euro(euros=1)
    cnt = currency.Euro(cents=100)

    assert eur == cnt


def test_euro_to_string():
    assert str(currency.Euro(0)) == '€0.00'
    assert str(currency.Euro(1)) == '€1.00'
    assert str(currency.Euro(0, 123)) == '€1.23'
    assert str(currency.Euro(12, 34)) == '€12.34'
    assert str(currency.Euro(1, 100)) == '€2.00'


def test_euro_from_string():
    with pytest.raises(ValueError):
        currency.Euro('foo')
    assert currency.Euro('0') == currency.Euro(0)
    assert currency.Euro('1') == currency.Euro(1)
    assert currency.Euro('12.34') == currency.Euro(12, 34)
    with pytest.raises(ValueError):
        currency.Euro('0.123')


def test_zero_is_its_own_instance():
    assert currency.Zero is currency.Zero()


def test_euros_can_be_added():
    a = currency.Euro(1)
    b = currency.Euro(2)
    assert a + b == currency.Euro(3)


def test_total_price_empty_basket():
    assert total_price([]) == currency.Euro(0)


def test_total_price_one_item():
    assert total_price([(1, currency.Euro(2))]) == currency.Euro(2)


def test_total_price_multiple_different_items():
    assert total_price([(3, currency.Euro(2)), (2, currency.Euro(cents=10))]) == currency.Euro('6.20')


def test_compute_tax():
    price = currency.Euro(1)
    tax = compute_tax(price, 0.01)
    assert tax == currency.Euro(cents=1)


def test_tax_rounds_down():
    price = currency.Euro(cents=20)
    tax = compute_tax(price, 0.19)
    assert tax == currency.Euro(cents=3)


def test_full_program_no_items():
    out = OutputSpy()
    inp = InputMock('0')

    main(IO(output=out, input=inp))

    assert out.buffers[1:] == ['Subtotal: €0.00\n',
                               'Tax: €0.00\n',
                               'Total: €0.00\n']


def test_full_program_three_items():
    out = OutputSpy()
    inp = InputMock('2', '25', '1', '10', '1', '4', '0')

    main(IO(output=out, input=inp))
    assert out.buffers[7:] == ['Subtotal: €64.00\n',
                               'Tax: €3.52\n',
                               'Total: €67.52\n']