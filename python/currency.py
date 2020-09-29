from __future__ import annotations

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Union
from numbers import Real

CENT_PER_UNIT = 100

UNIVERSAL_VALUE_UNIT_PER_CENT = 100000


class Currency(ABC):
    @staticmethod
    def zero() -> Currency: pass

    @abstractmethod
    def as_universal_value(self) -> int: pass

    @staticmethod
    @abstractmethod
    def from_universal_value(value: int) -> Currency: pass


class Zero(Currency):
    def as_universal_value(self) -> int:
        return 0

    @staticmethod
    def from_universal_value(_):
        raise ValueError("Not allowed")

    def __call__(self):
        return self

    def __eq__(self, other: Currency) -> bool:
        return other.as_universal_value() == 0

    def __add__(self, other: Currency) -> Currency:
        return other

    def __radd__(self, other: Currency) -> Currency:
        return other


Zero = Zero()


@dataclass
class CentBased(Currency):
    cents: int

    def __init__(self, symbol: str, unit: Union[int, str] = 0, cents: int = 0):
        self.symbol = symbol

        if isinstance(unit, str):
            assert cents == 0
            self.from_str(unit)
        else:
            self.cents = cents + unit * CENT_PER_UNIT

    def from_str(self, amount: str):
        numeric_amount = float(amount) * CENT_PER_UNIT
        cents = math.floor(numeric_amount)
        if cents != numeric_amount:
            raise ValueError(f'Invalid currency value: {amount}')
        self.cents = int(cents)

    def as_universal_value(self) -> int:
        return self.cents * UNIVERSAL_VALUE_UNIT_PER_CENT

    @classmethod
    def from_universal_value(cls, value: Real, round=math.floor) -> CentBased:
        return cls(cents=int(round(value / UNIVERSAL_VALUE_UNIT_PER_CENT)))

    def __str__(self) -> str:
        unit = self.cents // CENT_PER_UNIT
        cent = self.cents % CENT_PER_UNIT
        return f'{self.symbol}{unit}.{cent:0>2}'

    def __repr__(self) -> str:
        unit = self.cents // CENT_PER_UNIT
        cent = self.cents % CENT_PER_UNIT
        return f'{type(self).__name__}({unit}, {cent})'

    def __mul__(self, other: int) -> CentBased:
        cls = type(self)
        return cls(cents=self.cents * other)

    def __rmul__(self, other: int) -> CentBased:
        return self.__mul__(other)

    def __add__(self, other: Euro) -> CentBased:
        cls = type(self)
        assert isinstance(other, cls)
        return cls(cents=self.cents + other.cents)


class Euro(CentBased):
    def __init__(self, euros: Union[int, str] = 0, cents: int = 0):
        super().__init__(symbol='€', unit=euros, cents=cents)


class Dollar(CentBased):
    def __init__(self,  dollar: Union[int, str] = 0, cents: int = 0):
        super().__init__(symbol='$', unit=dollar, cents=cents)

    @staticmethod
    def convert_from(other: Currency, rate: float):
        x = other.as_universal_value()
        x *= rate
        return Dollar.from_universal_value(x, round=math.ceil)

