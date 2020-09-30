from python.myio import IO
from python.myio_testing import InputMock, OutputSpy
from python.exercise_12_interest_calculator import main


def test_full_program_three_items():
    out = OutputSpy()
    inp = InputMock('1500', '4.3', '4')

    main(IO(output=out, input=inp))
    assert out.buffers[3:] == ['After 4 years at 4.3%, the investment will be worth €1758.00.\n']
