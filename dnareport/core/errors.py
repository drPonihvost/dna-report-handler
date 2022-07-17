from typing import Any, List


class NameTypeError(Exception):
    def __init__(self, instance: Any, name: Any) -> None:
        self.name = name
        super().__init__(
            f"Incorrect name ({self.name}) type class {instance.__class__.__name__}, must be str,"
            f" not {type(name).__name__}"
        )


class DataTypeError(Exception):
    def __init__(self, value: Any) -> None:
        self.value = value
        self.message = self._create_message()
        super().__init__(self.message)

    def _create_message(self):
        return NotImplementedError(f"Implement method _create_message in {self.__class__.__name__}.")


class AlleleTypeError(DataTypeError):
    def _create_message(self):
        return f"Incorrect type in alleles, must be Allele, not {type(self.value).__name__}"


class AllelesDataTypeError(DataTypeError):
    def _create_message(self):
        return f"Incorrect type, must be List[Allele], not {type(self.value).__name__}"


class AlleleDataTypeError(DataTypeError):
    def _create_message(self):
        return f"Incorrect value ({self.value}) type class Allele, must be str, not {type(self.value).__name__}"


class MarkerDataTypeError(DataTypeError):
    def _create_message(self):
        return f"Incorrect value ({self.value}) type class Marker, must be Marker, not {type(self.value).__name__}"


class ParamError(DataTypeError):
    def _create_message(self):
        return f"Incorrect type ignore_merge_error, must be Boolean, not {type(self.value).__name__}"


class ObjectListTypeError(DataTypeError):
    def _create_message(self):
        return f"Incorrect objects type, must be Tuple[str], not {type(self.value).__name__}"


class GenotypeTypeError(DataTypeError):
    def _create_message(self):
        return f"Incorrect genotype, must be Genotype, not {type(self.value).__name__}"


class AlleleValueError(DataTypeError):
    def _create_message(self):
        return f"Incorrect value -> {self.value}"


class PathTypeError(DataTypeError):
    def _create_message(self):
        return f"path value must be str, not {type(self.value).__name__}"


class ExtensionError(DataTypeError):
    def _create_message(self):
        return f"Unsupported extension {self.value}"


class OpenFileError(Exception):
    def __init__(self, filename: str) -> None:
        self.filename = filename
        super().__init__(
            f"An error occurred while opening the file -> {self.filename}"
        )


class FileStructureError(Exception):
    def __init__(self) -> None:
        super().__init__(
            f"File structure error, possibly missing required fields"
        )


class MergeError(Exception):
    def __init__(self, current: List, other: List) -> None:
        self.current = current
        self.other = other
        super().__init__(
            f"Merge error current value {self.current} not equal {self.other}"
        )
