from datetime import datetime
from myio import IO
from myio_testing import InputMock, OutputSpy
from exercise_06_retirement_calculator import main


def test_invalid_numeric_input_ask_again():
    out = OutputSpy()
    inp = InputMock('foo', '42')
    io = IO(output=out, input=inp)

    n = io.input_number('number:')

    assert n == 42
    assert out.buffers == ['number:', 'number:']


def test_full_program():
    out = OutputSpy()
    inp = InputMock('25', '65')

    main(IO(output=out, input=inp), datetime(year=2015, month=2, day=3))

    assert out.buffers == ['What is your current age? ',
                          'At what age would you like to retire? ',
                          'You have 40 years left until you can retire.\n',
                          "It's 2015, so you can retire in 2055.\n"]
