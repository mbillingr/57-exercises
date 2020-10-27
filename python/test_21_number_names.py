import pytest
import math
from python.myio import IO
from python.myio_testing import InputMock, OutputSpy
from exercise_21_number_names import month


def test_zero_is_not_a_month():
    with pytest.raises(ValueError):
        month(0)


def test_there_are_no_13_months():
    with pytest.raises(ValueError):
        month(13)


def test_january():
    assert month(1) == 'January'


def test_february():
    assert month(2) == 'February'


def test_march():
    assert month(3) == 'March'


def test_april():
    assert month(4) == 'April'


def test_may():
    assert month(5) == 'May'


def test_june():
    assert month(6) == 'June'


def test_july():
    assert month(7) == 'July'


def test_august():
    assert month(8) == 'August'


def test_september():
    assert month(9) == 'September'


def test_october():
    assert month(10) == 'October'


def test_november():
    assert month(11) == 'November'


def test_december():
    assert month(12) == 'December'


def test_unknown_language():
    with pytest.raises(KeyError):
        month(3, 'foo')


def test_german():
    assert month(3, 'de') == 'März'
