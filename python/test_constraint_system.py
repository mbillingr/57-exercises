import pytest
from constraint_system import Variable, Constant, ContradictionError, Equal, Adder, Multiplier


def test_new_connectors_are_distinct_objects():
    a = Variable()
    b = Variable()
    assert a is not b


def test_new_connector_has_no_value():
    c = Variable()
    assert not c.has_value()


def test_getting_no_value_raises_exception():
    c = Variable()
    with pytest.raises(ValueError):
        c.get_value()


def test_setting_a_value():
    c = Variable()
    c.set_value(0)
    assert c.has_value()


def test_getting_a_value():
    c = Variable()
    c.set_value(1)
    assert c.get_value() == 1


def test_none_is_a_valid_value():
    c = Variable()
    c.set_value(None)
    assert c.get_value() is None


def test_forget_a_value():
    c = Variable()
    c.set_value(0)
    c.forget_value()
    assert not c.has_value()


def test_constant_constraint():
    a = Variable()
    c = Constant(0, a)
    assert a.get_value() == 0


def test_conflicting_constraint():
    a = Variable()
    Constant(0, a)
    with pytest.raises(ContradictionError):
        Constant(1, a)


def test_equality_constraint():
    a = Variable()
    b = Variable()
    c = Equal(a, b)

    a.set_value(0)
    assert b.get_value() == 0

    with pytest.raises(ContradictionError):
        b.set_value(1)

    a.forget_value()
    b.set_value(1)
    assert a.get_value() == 1


def test_constant_constraint_cant_set():
    a = Variable()
    c = Constant(0, a)
    with pytest.raises(ContradictionError):
        a.set_value(1)
    assert a.get_value() == 0


def test_constant_constraint_cant_forget():
    a = Variable()
    c = Constant(0, a)
    a.forget_value()
    assert a.get_value() == 0


def test_adder_constraint_no_values():
    a = Variable()
    b = Variable()
    c = Variable()
    Adder(a, b, c)
    assert not a.has_value()
    assert not b.has_value()
    assert not c.has_value()


def test_adder_constraint_adds_values():
    a = Variable()
    b = Variable()
    c = Variable()
    Adder(a, b, c)

    a.set_value(1)
    assert a.get_value() == 1
    assert not b.has_value()
    assert not c.has_value()

    b.set_value(2)
    assert a.get_value() == 1
    assert b.get_value() == 2
    assert c.get_value() == 3


def test_adder_constraint_subtracts_first_value():
    a = Variable()
    b = Variable()
    c = Variable()
    Adder(a, b, c)

    a.set_value(1)
    c.set_value(0)
    assert b.get_value() == -1


def test_adder_constraint_subtracts_second_value():
    a = Variable()
    b = Variable()
    c = Variable()
    Adder(a, b, c)

    b.set_value(1)
    c.set_value(0)
    assert a.get_value() == -1


def test_adder_forget_value():
    a = Variable()
    b = Variable()
    c = Variable()
    Adder(a, b, c)

    a.set_value(1)
    b.set_value(1)
    assert c.has_value()

    a.forget_value()
    assert not c.has_value()


def test_adder_sequence():
    a = Variable()
    b = Variable()
    c = Variable()
    sum = Variable()
    tmp = Variable()
    Adder(a, b, tmp)
    Adder(tmp, c, sum)

    a.set_value(1)
    b.set_value(2)
    c.set_value(3)
    assert tmp.get_value() == 3
    assert sum.get_value() == 6

    a.forget_value()
    sum.set_value(5)
    assert tmp.get_value() == 2
    assert a.get_value() == 0


def test_syntactic_sugar_add():
    a = Variable()
    b = Variable()
    c = a + b

    assert isinstance(c, Variable)
    assert not c.has_value()

    a.set_value(2)
    b.set_value(3)
    assert c.get_value() == 5


def test_syntactic_sugar_add_constant():
    a = Variable()
    b = a + 1

    assert not b.has_value()

    a.set_value(1)
    assert b.get_value() == 2


def test_syntactic_sugar_radd_constant():
    a = Variable()
    b = 1 + a

    assert not b.has_value()

    a.set_value(1)
    assert b.get_value() == 2


def test_add_strings():
    a = Variable()
    b = a + 'bar'

    a.set_value('foo')
    assert b.get_value() == 'foobar'


def test_addsubtract_strings():
    a = Variable()
    b = a + 'bar'

    b.set_value('foobar')
    assert a.get_value() == 'foo'


def test_addsubtract_strings_right():
    a = Variable()
    b = 'foo' + a

    b.set_value('foobar')
    assert a.get_value() == 'bar'


def test_addsubtract_strings_invalid():
    a = Variable()
    b = a + 'xyz'

    with pytest.raises(ContradictionError):
        b.set_value('foobar')


def test_multiplier_constraint_no_values():
    a = Variable()
    b = Variable()
    c = Variable()
    Multiplier(a, b, c)
    assert not a.has_value()
    assert not b.has_value()
    assert not c.has_value()


def test_multiplier_constraint_adds_values():
    a = Variable()
    b = Variable()
    c = Variable()
    Multiplier(a, b, c)

    a.set_value(2)
    assert a.get_value() == 2
    assert not b.has_value()
    assert not c.has_value()

    b.set_value(3)
    assert a.get_value() == 2
    assert b.get_value() == 3
    assert c.get_value() == 6


def test_syntactic_sugar_mul():
    a = Variable()
    b = Variable()
    c = a * b

    assert isinstance(c, Variable)
    assert not c.has_value()

    a.set_value(2)
    b.set_value(3)
    assert c.get_value() == 6


def test_syntactic_sugar_sub():
    a = Variable()
    b = Variable()
    c = a - b

    a.set_value(3)
    b.set_value(2)
    assert c.get_value() == 1


def test_syntactic_sugar_sub_string_right1():
    a = Variable()
    c = a - 'bar'

    a.set_value('foobar')
    assert c.get_value() == 'foo'


def test_syntactic_sugar_sub_string_right2():
    a = Variable()
    c = 'foobar' - a

    a.set_value('bar')
    assert c.get_value() == 'foo'


def test_string_multiply_number_left():
    a = Variable()
    b = Variable()
    c = a * b

    a.set_value('foo')
    c.set_value('foofoofoo')
    assert b.get_value() == 3


def test_string_multiply_number_right():
    a = Variable()
    b = Variable()
    c = a * b

    b.set_value('foo')
    c.set_value('foofoofoo')
    assert a.get_value() == 3


def test_regression():
    x = Variable()
    slope = Variable()
    offset = Variable()

    offset.set_value(1)
    slope.set_value(2)
    y = offset + x * slope

    x.set_value(1)
    assert y.get_value() == 3

    x.forget_value()
    y.set_value(5)
    assert x.get_value() == 2

    slope.forget_value()
    slope.set_value(1)
    y.set_value(5)
    assert x.get_value() == 4
