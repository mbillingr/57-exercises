from datetime import datetime
from myio import IO
from numbers import Number


def main(io: IO, date: datetime):
    age = io.input_number('What is your current age? ')
    ret = io.input_number('At what age would you like to retire? ')

    years_to_work = ret - age
    retirement_year = date.year + years_to_work

    io.println(f"You have {years_to_work} years left until you can retire.")
    io.println(f"It's {date.year}, so you can retire in {retirement_year}.")


if __name__ == '__main__':
    main(IO(), datetime.now())
