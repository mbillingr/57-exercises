import pytest
import math
from python.myio import IO
from python.myio_testing import InputMock, OutputSpy
from exercise_22_number_compare import larger, largest


def test_larger_of_same_numbers():
    assert larger(1, 1) == 1


def test_second_is_larger():
    assert larger(1, 2) == 2


def test_first_is_larger():
    assert larger(3, 2) == 3


def test_larger_ignores_none():
    assert larger(1, None) == 1
    assert larger(None, 2) == 2


def test_largest_empty():
    assert largest([]) is None


def test_largest_one_item_is_same():
    assert largest([1]) == 1


def test_largest_of_two_items():
    assert largest([1, 2]) == 2


def test_largest_of_three_items():
    assert largest([1, 2, 3]) == 3


def test_largest_of_many_items():
    assert largest([7, 5, 3, 1, 9, 0, 2, 4, 6, 8]) == 9
