from numbers import Real
from myio import IO
import math


GALLONS_PER_SQUARE_FEET = 1 / 350


def paint_needed(area: Real) -> int:
    return math.ceil(area * GALLONS_PER_SQUARE_FEET)


def main(io: IO):
    length = io.input_number('What is the length of the room in feet? ')
    width = io.input_number('What is the width of the room in feet? ')

    area_in_square_feet = length * width
    gallons_of_paint = paint_needed(area_in_square_feet)

    io.println(f"You will need to purchase {gallons_of_paint} gallons of paint"
               f" to cover {area_in_square_feet} square feet.")


if __name__ == '__main__':
    main(IO())
