from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Any


class ContradictionError(Exception):
    def __init__(self, *conflicts):
        self.conflicts = conflicts


class User:
    __instance = None

    def __new__(cls):
        if User.__instance is None:
            User.__instance = object.__new__(User)
        return User.__instance


class Variable:
    def __init__(self):
        self.value = None
        self.informant = None
        self.constraints = set()

    def has_value(self) -> bool:
        return self.informant is not None

    def get_value(self) -> Any:
        if self.has_value():
            return self.value
        raise ValueError("No value")

    def reset_value(self, value: Any, informer: Constraint | User = User()):
        self.forget_value(informer)
        self.set_value(value, informer)

    def set_value(self, value: Any, informer: Constraint | User = User()):
        if not self.has_value():
            self.value = value
            self.informant = informer
            for c in self.constraints:
                if c is not informer:
                    c.process_new_value()
        elif value != self.value:
            raise ContradictionError()

    def forget_value(self, retractor: Constraint | User = User()):
        if retractor is self.informant:
            self.informant = None
            self.value = None
            for c in self.constraints:
                c.process_forget_value()

    def connect(self, constraint: Constraint):
        if not constraint in self.constraints:
            self.constraints.add(constraint)

    def __add__(self, other):
        if isinstance(other, Variable):
            sum = Variable()
            Adder(self, other, sum)
            return sum
        else:
            tmp = Variable()
            Constant(other, tmp)
            return self + tmp

    def __radd__(self, other):
        if isinstance(other, Variable):
            sum = Variable()
            Adder(other, self, sum)
            return sum
        else:
            tmp = Variable()
            Constant(other, tmp)
            return tmp + self

    def __mul__(self, other):
        if isinstance(other, Variable):
            prod = Variable()
            Multiplier(self, other, prod)
            return prod
        else:
            tmp = Variable()
            Constant(other, tmp)
            return self * tmp

    def __rmul__(self, other):
        if isinstance(other, Variable):
            prod = Variable()
            Multiplier(other, self, prod)
            return prod
        else:
            tmp = Variable()
            Constant(other, tmp)
            return tmp * self

    def __sub__(self, other):
        if isinstance(other, Variable):
            left = Variable()
            Adder(left, other, self)
            return left
        else:
            tmp = Variable()
            Constant(other, tmp)
            return self - tmp

    def __rsub__(self, other):
        if isinstance(other, Variable):
            right = Variable()
            Adder(other, right, self)
            return right
        else:
            tmp = Variable()
            Constant(other, tmp)
            return tmp - self

    def __div__(self, other):
        if isinstance(other, Variable):
            left = Variable()
            Multiplier(left, other, self)
            return left
        else:
            tmp = Variable()
            Constant(other, tmp)
            return self / tmp

    def __rdiv__(self, other):
        if isinstance(other, Variable):
            right = Variable()
            Multiplier(other, right, self)
            return right
        else:
            tmp = Variable()
            Constant(other, tmp)
            return tmp / self


class Constraint:
    def process_new_value(self):
        raise NotImplementedError("Subclass Responsibility")

    def process_forget_value(self):
        raise NotImplementedError("Subclass Responsibility")


class Constant(Constraint):
    def __init__(self, value: Any, connector: Variable):
        connector.connect(self)
        connector.set_value(value, informer=self)

    def process_new_value(self):
        raise ContradictionError()

    def process_forget_value(self):
        raise ContradictionError()


class Equal(Constraint):
    def __init__(self, a: Variable, b: Variable):
        self.a = a
        self.b = b
        a.connect(self)
        b.connect(self)

    def process_new_value(self):
        if self.a.has_value():
            self.b.set_value(self.a.get_value(), informer=self)
        elif self.b.has_value():
            self.a.set_value(self.b.get_value(), informer=self)

    def process_forget_value(self):
        self.a.forget_value(self)
        self.b.forget_value(self)


class Adder(Constraint):
    def __init__(self, a: Variable, b: Variable, c: Variable):
        self.a = a
        self.b = b
        self.c = c
        a.connect(self)
        b.connect(self)
        c.connect(self)

    def process_new_value(self):
        if self.a.has_value() and self.b.has_value():
            left = self.a.get_value()
            right = self.b.get_value()
            self.c.set_value(GenericAdd.dispatch(left, right), self)
        elif self.a.has_value() and self.c.has_value():
            left2 = self.c.get_value()
            right2 = self.a.get_value()
            self.b.set_value(GenericLSub.dispatch(left2, right2), self)
        elif self.b.has_value() and self.c.has_value():
            left1 = self.c.get_value()
            right1 = self.b.get_value()
            self.a.set_value(GenericRSub.dispatch(left1, right1), self)

    def process_forget_value(self):
        self.a.forget_value(self)
        self.b.forget_value(self)
        self.c.forget_value(self)
        self.process_new_value()


class Multiplier(Constraint):
    def __init__(self, a: Variable, b: Variable, c: Variable):
        self.a = a
        self.b = b
        self.c = c
        a.connect(self)
        b.connect(self)
        c.connect(self)

    def process_new_value(self):
        if self.a.has_value() and self.b.has_value():
            left = self.a.get_value()
            right = self.b.get_value()
            self.c.set_value(GenericMul.dispatch(left, right), self)
        elif self.a.has_value() and self.c.has_value():
            left1 = self.c.get_value()
            right1 = self.a.get_value()
            self.b.set_value(GenericLDiv.dispatch(left1, right1), self)
        elif self.b.has_value() and self.c.has_value():
            left2 = self.c.get_value()
            right2 = self.b.get_value()
            self.a.set_value(GenericRDiv.dispatch(left2, right2), self)

    def process_forget_value(self):
        self.a.forget_value(self)
        self.b.forget_value(self)
        self.c.forget_value(self)
        self.process_new_value()


def register_op(op, left_type, right_type, method):
    op.register(left_type, right_type, method)


class GenericOp(metaclass=ABCMeta):
    _methods = None

    @classmethod
    def register(cls, left_type, right_type, method):
        cls._methods[(left_type, right_type)] = method

    @classmethod
    def dispatch(cls, left, right):
        method = cls._methods.get((type(left), type(right)), cls.default)
        return method(left, right)

    @staticmethod
    @abstractmethod
    def default(left, right):
        pass


class GenericAdd(GenericOp):
    _methods = {}

    @staticmethod
    def default(left, right):
        return left + right


class GenericRSub(GenericOp):
    _methods = {}

    @staticmethod
    def default(left, right):
        return left - right


class GenericLSub(GenericOp):
    _methods = {}

    @staticmethod
    def default(left, right):
        return left - right


class GenericMul(GenericOp):
    _methods = {}

    @staticmethod
    def default(left, right):
        return left * right


class GenericLDiv(GenericOp):
    _methods = {}

    @staticmethod
    def default(left, right):
        return left / right


class GenericRDiv(GenericOp):
    _methods = {}

    @staticmethod
    def default(left, right):
        return left / right


def string_div(left: str, right: str) -> int:
    n = 0
    while left.startswith(right):
        left = left[len(right):]
        n += 1
    if not left:
        return n
    raise ContradictionError(left, right)


def string_rsub(left: str, right: str) -> str:
    if left.endswith(right):
        return left[:len(right)]
    raise ContradictionError(left, right)


def string_lsub(left: str, right: str) -> str:
    if left.startswith(right):
        return left[len(right):]
    raise ContradictionError(left, right)


register_op(GenericRSub, str, str, string_rsub)
register_op(GenericLSub, str, str, string_lsub)

register_op(GenericLDiv, str, str, string_div)
register_op(GenericRDiv, str, str, string_div)
