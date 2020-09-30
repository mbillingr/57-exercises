from python.myio import IO
from python.myio_testing import InputMock, OutputSpy
from python.exercise_13_compound_interest import get_inputs, format_output, compute_compound_interest, main


def test_get_inputs():
    out = OutputSpy()
    inp = InputMock('15', '4.32', '2', '3')
    p, r, t, n = get_inputs(IO(output=out, input=inp))

    assert p == 15
    assert r == 4.32
    assert t == 2
    assert n == 3


def test_format_output():
    output = format_output(principal=1, rate_percent=2, years=3, compounds=4, final_value=5)
    assert output == '1 invested at 2% for 3 years compounded 4 times per year is 5.'


def test_compute_compound_interest():
    final_value = compute_compound_interest(principal=1, rate=0.1, years=1, compounds=1)
    assert final_value == 1.1


def test_full_program_three_items():
    out = OutputSpy()
    inp = InputMock('1500', '4.3', '6', '4')

    main(IO(output=out, input=inp))
    assert out.buffers[4:] == ['€1500.00 invested at 4.3% for 6 years compounded 4 times per year is €1938.84.\n']
