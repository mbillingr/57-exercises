from python.myio import IO
from python.myio_testing import InputMock, OutputSpy
from python.exercise_02_count_chars import main, count_chars


def test_count_chars_empty_string():
    assert count_chars('') == 0


def test_count_chars_ascii_string():
    assert count_chars('foobar') == 6


def test_count_chars_unicode():
    assert count_chars('äöüß') == 4


def test_full_program():
    out = OutputSpy()
    inp = InputMock('Homer')

    main(IO(output=out, input=inp))

    assert out.buffers == ['What is the input string? ',
                          'Homer has 5 characters\n']


def test_challenge_empty_input():
    out = OutputSpy()
    inp = InputMock()

    main(IO(output=out, input=inp))

    assert out.buffers == ['What is the input string? ',
                          'You must enter something.\n']
