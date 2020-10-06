from python.exercise_16_driving_age import get_inputs, may_drive, main
from python.myio import IO
from python.myio_testing import InputMock, OutputSpy


def test_get_inputs():
    out = OutputSpy()
    inp = InputMock('42')
    age = get_inputs(IO(output=out, input=inp))

    assert age == 42


def test_may_drive_too_youngs():
    assert not may_drive(15)


def test_may_drive():
    assert may_drive(16)


def test_full_program_may_not_drive():
    out = OutputSpy()
    inp = InputMock('15')

    main(IO(output=out, input=inp))
    assert out.buffers[1:] == ["You are not old enough to legally drive.\n"]


def test_full_program_may_drive():
    out = OutputSpy()
    inp = InputMock('16')

    main(IO(output=out, input=inp))
    assert out.buffers[1:] == ["You are old enough to legally drive.\n"]
