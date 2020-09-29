from abc import ABC, abstractmethod
from numbers import Real


class OutputInterface(ABC):
    @abstractmethod
    def write(self, s): pass


class InputInterface(ABC):
    @abstractmethod
    def get_line(self): pass


class ConsoleOutput(OutputInterface):
    def write(self, s):
        print(s, end='')


class ConsoleInput(InputInterface):
    def get_line(self):
        return input()


class IO:
    def __init__(self,
                 output: OutputInterface = ConsoleOutput(),
                 input: InputInterface = ConsoleInput()):
        self.out = output
        self.inp = input

    def input_number(self, prompt: str) -> Real:
        while True:
            try:
                return string_to_number(self.input(prompt))
            except ValueError:
                pass

    def input(self, prompt: str = '>> ') -> str:
        self.print(prompt)
        return self.inp.get_line()

    def print(self, s: str):
        self.out.write(s)

    def println(self, s: str):
        self.print(s + '\n')


def string_to_number(s: str) -> Real:
    try:
        return int(s)
    except ValueError:
        pass

    return float(s)
