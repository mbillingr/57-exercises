import pytest
from python.myio import IO
from python.myio_testing import InputMock, OutputSpy
from python.exercise_01_say_hello import main


def test_produce_output():
    out = OutputSpy()
    out.write('Foo')
    assert out.buffers == ['Foo']


def test_request_input_eof():
    inp = InputMock()
    with pytest.raises(EOFError):
        inp.get_line()


def test_request_input():
    inp = InputMock('Bar')
    assert inp.get_line() == 'Bar'
    with pytest.raises(EOFError):
        inp.get_line()


def test_request_input_twice():
    inp = InputMock('Foo\nBar')
    assert inp.get_line() == 'Foo'
    assert inp.get_line() == 'Bar'


def test_request_input_twice_from_list():
    inp = InputMock('Bar', 'Baz')
    assert inp.get_line() == 'Bar'
    assert inp.get_line() == 'Baz'


def test_prompt():
    out = OutputSpy()
    inp = InputMock('Bar')
    io = IO(output=out, input=inp)

    answer = io.input('Foo?')

    assert out.buffers == ['Foo?']
    assert answer == 'Bar'


def test_default_prompt():
    out = OutputSpy()
    inp = InputMock('42')
    io = IO(output=out, input=inp)

    answer = io.input()

    assert out.buffers == ['>> ']
    assert answer == '42'


def test_print():
    out = OutputSpy()
    inp = InputMock()
    io = IO(output=out, input=inp)

    io.print('Foo')

    assert out.buffers == ['Foo']


def test_println():
    out = OutputSpy()
    inp = InputMock()
    io = IO(output=out, input=inp)

    io.println('Foo')

    assert out.buffers == ['Foo\n']


def test_full_program():
    out = OutputSpy()
    inp = InputMock('Brian')

    main(IO(output=out, input=inp))

    assert out.buffers == ['What is your name? ',
                          'Hello, Brian, nice to meet you!\n']
