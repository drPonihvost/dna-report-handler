from dataclasses import dataclass

from dnareport.core.base import Name
from dnareport.core.errors import AlleleValueError, DataTypeError


@dataclass
class Allele(Name):
    _value: str

    def __post_init__(self):
        super().__post_init__()
        self.__check_value(self._value)

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        self.__check_value(value)
        self._value = value

    @staticmethod
    def _check_name(name: str) -> None:
        if not isinstance(name, str):
            raise ValueError

    @staticmethod
    def __check_value(value):
        if not isinstance(value, str):
            raise DataTypeError
        if len(value) > 4:
            raise AlleleValueError

    def to_dict(self) -> dict:
        return {'name': self.name, 'value': self.value}


a1 = Allele('Allele 1', '15')
a2 = Allele('Allele 2', '17')

