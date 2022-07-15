from dataclasses import dataclass


@dataclass
class Name:
    _name: str

    def __post_init__(self):
        self._check_name(self.name)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._check_name(name)
        self._name = name

    def _check_name(self, name: str) -> Exception or None:
        raise NotImplementedError(f"Определите _check_name в {self.__class__.__name__}.")
