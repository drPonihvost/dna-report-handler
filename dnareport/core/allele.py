from dataclasses import dataclass

from dnareport.core.errors import AlleleValueError, AlleleDataTypeError


@dataclass
class Allele:
    _value: str

    def __post_init__(self) -> None:
        self.__check_value(self._value)

    @property
    def value(self) -> str:
        return self._value

    @staticmethod
    def __check_value(value: str) -> Exception or None:
        if not isinstance(value, str):
            raise AlleleDataTypeError(value)
        if len(value) > 4:
            raise AlleleValueError(value)

    def __hash__(self):
        return hash(self._value)

    def __str__(self):
        return f"class {self.__class__.__name__} value: {self._value}"
