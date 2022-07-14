from dataclasses import dataclass, field
from typing import List, Dict

from dnareport.core.base import Name
from dnareport.core.errors import GenotypeNameError, DataTypeError
from dnareport.core.marker import Marker


@dataclass
class Genotype(Name):
    _markers: List[Marker] = field(default_factory=list, init=False)

    def __post_init__(self):
        super().__post_init__()

    @property
    def markers(self) -> List[Marker] or None:
        return self._markers

    @staticmethod
    def __check_marker(marker: Marker) -> Exception or None:
        if not isinstance(marker, Marker):
            raise DataTypeError

    @staticmethod
    def _check_name(name: str) -> GenotypeNameError or None:
        if not isinstance(name, str):
            raise GenotypeNameError

    def __is_duplicate(self, marker: Marker) -> bool:
        return marker in self._markers

    def __get_marker_by_name(self, name: str) -> Marker:
        for marker in self._markers:
            if marker.name == name:
                return marker

    def add_marker(self, marker: Marker) -> None:
        self.__check_marker(marker)
        if self._markers:
            current_marker = self.__get_marker_by_name(marker.name)
            if current_marker:
                current_marker.merge(marker.alleles)
                return
        self.markers.append(marker)

    def to_dict(self) -> Dict:
        return {'name': self.name, 'markers': [marker.to_dict() for marker in self._markers]}
