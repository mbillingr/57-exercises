from python.exercise_15_password_validation import get_inputs, validate, main
from python.myio import IO
from python.myio_testing import InputMock, OutputSpy


def test_get_inputs():
    out = OutputSpy()
    inp = InputMock('foobar$0815')
    pw = get_inputs(IO(output=out, input=inp))

    assert pw == 'foobar$0815'


def test_validate_no_pw():
    assert not validate('')


def test_validate_wrong_pw():
    assert not validate('foo')


def test_validate_correct_pw():
    assert validate('abc$123')


def test_full_program_wrong_pass():
    out = OutputSpy()
    inp = InputMock('12345')

    main(IO(output=out, input=inp))
    assert out.buffers[1:] == ["I don't know you.\n"]


def test_full_program_right_pass():
    out = OutputSpy()
    inp = InputMock('abc$123')

    main(IO(output=out, input=inp))
    assert out.buffers[1:] == ["Welcome!\n"]
