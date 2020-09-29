import pytest
from myio import IO
from myio_testing import InputMock, OutputSpy
from exercise_05_simple_math import main, string_to_number


def test_string_to_number_fails_for_invalid_string():
    with pytest.raises(ValueError):
        string_to_number('foo')


def test_string_to_digit():
    assert string_to_number('0') == 0


def test_string_to_negative_number():
    assert string_to_number('-123') == -123


def test_string_to_float():
    assert string_to_number('1.2') == 1.2


def test_scientific_notation():
    assert string_to_number('-1e-2') == -0.01


def test_full_program():
    out = OutputSpy()
    inp = InputMock('10', '5')

    main(IO(output=out, input=inp))

    assert out.buffers == ['What is the first number? ',
                          'What is the second number? ',
                          '10 + 5 = 15\n10 - 5 = 5\n10 * 5 = 50\n10 / 5 = 2\n']
