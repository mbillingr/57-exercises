from python.myio import IO
from python.myio_testing import InputMock, OutputSpy
from exercise_18_temperature_convert import temperature, main


def test_convert_from_fahrenheit():
    c, f, k = temperature()

    f.set_value(32)
    assert c.get_value() == 0
    assert k.get_value() == 273.15

    f.reset_value(100)
    assert c.get_value() == (100 - 32) * 5 / 9
    assert k.get_value() == (100 - 32) * 5 / 9 + 273.15


def test_convert_from_celsius():
    c, f, k = temperature()

    c.set_value(0)
    assert f.get_value() == 32
    assert k.get_value() == 273.15

    c.reset_value(100)
    assert f.get_value() == 100 * 9 / 5 + 32
    assert k.get_value() == 373.15


def test_full_program_f_to_c():
    out = OutputSpy()
    inp = InputMock('F', 'C', '100')

    main(IO(output=out, input=inp))
    assert out.buffers[2:] == ["Please enter the temperature in Fahrenheit: ",
                               "The temperature in Celsius is 37.8.\n"]


def test_full_program_c_to_f():
    out = OutputSpy()
    inp = InputMock('C', 'F', '100')

    main(IO(output=out, input=inp))
    assert out.buffers[2:] == ["Please enter the temperature in Celsius: ",
                               "The temperature in Fahrenheit is 212.0.\n"]
