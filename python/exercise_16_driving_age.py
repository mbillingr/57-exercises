from python.myio import IO


def get_inputs(io: IO) -> str:
    pw = io.input_number('What is your age? ')
    return pw


def may_drive(age: int):
    return age >= 16


def main(io: IO):
    age = get_inputs(io)
    denial = "" if may_drive(age) else " not"
    io.println(f"You are{denial} old enough to legally drive.")


if __name__ == '__main__':
    main(IO())
