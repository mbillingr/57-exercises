from constraint_system import Variable, Equal
from python.myio import IO


def temperature() -> (Variable, Variable):
    c = Variable()
    f = Variable()
    k = Variable()

    Equal(c * 9, (f - 32) * 5)
    Equal(k, c + 273.15)

    return c, f, k


UNITS = {'F': 'Fahrenheit', 'C': 'Celsius', 'K': 'Kelvin'}


def main(io: IO):
    conversion_input = io.input("Enter temperature unit to convert from (F/C/K): ")
    conversion_output = io.input("Enter temperature unit to convert to (F/C/K): ")

    c, f, k = temperature()
    variables = {'F': f, 'C': c, 'K': k}

    input_unit = UNITS[conversion_input]
    output_unit = UNITS[conversion_output]
    i = variables[conversion_input]
    o = variables[conversion_output]

    in_temp = io.input_number(f"Please enter the temperature in {input_unit}: ")

    i.set_value(in_temp)
    out_temp = o.get_value()

    io.println(f"The temperature in {output_unit} is {out_temp :.1f}.")


if __name__ == '__main__':
    main(IO())
