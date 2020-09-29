from python.myio import IO
from python.myio_testing import InputMock, OutputSpy
from python.exercise_09_paint_calculator import paint_needed, main


SQUARE_FEET_PER_GALLON = 350


def test_no_area_no_paint():
    assert paint_needed(0) == 0


def test_small_area_at_least_one_gallon():
    assert paint_needed(0.1) == 1


def test_larger_area_need_another_gallon():
    assert paint_needed(SQUARE_FEET_PER_GALLON + 0.1) == 2


def test_full_program():
    out = OutputSpy()
    inp = InputMock('18', '20')

    main(IO(output=out, input=inp))

    assert out.buffers[2:] == ['You will need to purchase 2 gallons of '
                               'paint to cover 360 square feet.\n']
