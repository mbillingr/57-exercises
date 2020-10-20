import math
from python.myio import IO
from python.myio_testing import InputMock, OutputSpy
from exercise_19_bmi_calculator import calculate_bmi, classify_bmi


def test_calculate_bmi():
    assert math.isclose(calculate_bmi(weight=1, height=1), 703)
    assert math.isclose(calculate_bmi(weight=1/703, height=1), 1)
    assert math.isclose(calculate_bmi(weight=1/703, height=2), 2**-2)
    assert math.isclose(calculate_bmi(weight=3, height=math.sqrt(703)), 3)


def test_classify_bmi():
    assert classify_bmi(18.499) == 'underweight'
    assert classify_bmi(18.500) == 'ideal'
    assert classify_bmi(25.000) == 'ideal'
    assert classify_bmi(25.001) == 'overweight'
