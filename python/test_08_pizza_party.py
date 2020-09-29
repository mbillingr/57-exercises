import pytest

from python.exercise_08_pizza_party import divide_pizzas, main
from python.myio import IO
from python.myio_testing import InputMock, OutputSpy
from python.pluralize import pluralize


def test_no_people_eat_no_pizzas():
    with pytest.raises(ValueError):
        divide_pizzas(n_people=0, n_pizzas=0, n_pieces=0)


def test_all_for_one():
    person_pieces, leftover = divide_pizzas(n_people=1, n_pizzas=2, n_pieces=3)

    assert leftover == 0
    assert person_pieces == 2 * 3


def test_two_people_eat_all():
    person_pieces, leftover = divide_pizzas(n_people=2, n_pizzas=2, n_pieces=3)

    assert leftover == 0
    assert person_pieces == 3


def test_two_people_eat_part():
    person_pieces, leftover = divide_pizzas(n_people=2, n_pizzas=3, n_pieces=3)

    assert leftover == 1
    assert person_pieces == 4


def test_stringify_people():
    assert pluralize(2, 'people') == 'people'


def test_stringify_one_people():
    assert pluralize(1, 'people') == 'person'


def test_stringify_pizza():
    assert pluralize(1, 'pizza') == 'pizza'


def test_stringify_pizzas():
    assert pluralize(2, 'pizza') == 'pizzas'


def test_bigger_divide():
    person_pieces, leftover = divide_pizzas(n_people=7, n_pizzas=2, n_pieces=8)

    assert leftover == 2
    assert person_pieces == 2


def test_full_program():
    out = OutputSpy()
    inp = InputMock('7', '2', '8')

    main(IO(output=out, input=inp))

    assert out.buffers[3:] == ['7 people with 2 pizzas\n',
                               'Each person gets 2 pieces of pizza.\n',
                               'There are 2 leftover pieces.\n']
