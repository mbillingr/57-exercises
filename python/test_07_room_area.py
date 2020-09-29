from python.exercise_07_room_area import main, square_feet_to_square_meters
from python.myio import IO
from python.myio_testing import InputMock, OutputSpy


def test_metric_conversion_zero():
    assert square_feet_to_square_meters(0) == 0


def test_one_square_foot_to_square_meters():
    assert square_feet_to_square_meters(1) == 0.09290304


def test_full_program():
    out = OutputSpy()
    inp = InputMock('15', '20')

    main(IO(output=out, input=inp))

    assert out.buffers[2:] == ['You entered dimensions of 15 feet by 20 feet.\n',
                               'The area is\n',
                               '300 square feet\n',
                               '27.871 square meters\n']
