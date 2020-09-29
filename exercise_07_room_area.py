from myio import IO
from numbers import Number


SQUARE_METERS_PER_SQUARE_FOOT = 0.09290304


def square_feet_to_square_meters(f2: Number) -> Number:
    return f2 * SQUARE_METERS_PER_SQUARE_FOOT


def main(io: IO):
    length = io.input_number('What is the length of the room in feet? ')
    width = io.input_number('What is the width of the room in feet? ')

    area_in_square_feet = length * width
    area_in_square_meters = square_feet_to_square_meters(area_in_square_feet)

    io.println(f"You entered dimensions of {length} feet by {width} feet.")
    io.println(f"The area is")
    io.println(f"{area_in_square_feet} square feet")
    io.println(f"{area_in_square_meters:.3f} square meters")


if __name__ == '__main__':
    main(IO())
