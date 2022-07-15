from typing import Any


class DataTypeError(Exception):
    pass


class AlleleDataTypeError(DataTypeError):
    def __init__(self, value: Any) -> None:
        self.value = value
        super().__init__(
            f"Incorrect value ({self.value}) type class Allele, must be str,"
            f" not {type(value).__name__}"
        )


class AlleleValueError(ValueError):
    def __init__(self, value: Any) -> None:
        self.value = value
        super().__init__(f"Incorrect value -> {self.value}")


class GenotypeNameError(ValueError):
    pass


class ReportNameError(ValueError):
    pass


class MergeError(ValueError):
    pass
