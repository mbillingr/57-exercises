from python.myio import InputInterface, OutputInterface


class OutputSpy(OutputInterface):
    def __init__(self):
        self.buffers = []

    def write(self, s: str):
        self.buffers.append(s)


class InputMock(InputInterface):
    def __init__(self, *args):
        self.lines = [line for part in args for line in part.splitlines()]

    def get_line(self):
        if not self.lines:
            raise EOFError
        return self.lines.pop(0)
