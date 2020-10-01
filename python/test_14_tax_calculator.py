from python.myio import IO
from python.myio_testing import InputMock, OutputSpy
from python.exercise_14_tax_calculator import get_inputs, format_output, compute_tax, main


def test_get_inputs():
    out = OutputSpy()
    inp = InputMock('1', 'foo')
    amount, state = get_inputs(IO(output=out, input=inp))

    assert amount == 1
    assert state == 'FOO'


def test_format_output_total_only():
    output = format_output(total=1)
    assert output == 'The total is 1.'


def test_format_output_taxed():
    output = format_output(total=1, subtotal=2, tax=3)
    assert output == 'The subtotal is 2.\nThe tax is 3.\nThe total is 1.'


def test_compute_default_tax():
    total, subtotal, tax = compute_tax(amount=1, state='FOO')

    assert subtotal is None
    assert tax is None
    assert total == 1


def test_compute_wi_tax():
    total, subtotal, tax = compute_tax(amount=10, state='WI')

    assert subtotal == 10
    assert tax == 0.55
    assert total == subtotal + tax


def test_full_program_wi():
    out = OutputSpy()
    inp = InputMock('10', 'wi')

    main(IO(output=out, input=inp))
    assert out.buffers[2:] == ['The subtotal is $10.00.\nThe tax is $0.55.\nThe total is $10.55.\n']


def test_full_program_ba():
    out = OutputSpy()
    inp = InputMock('10', 'ba')

    main(IO(output=out, input=inp))
    assert out.buffers[2:] == ['The total is $10.00.\n']
