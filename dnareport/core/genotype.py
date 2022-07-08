from dataclasses import dataclass
from typing import List

from dnareport.core.base import Name
from dnareport.core.errors import GenotypeNameError, DataTypeError
from dnareport.core.marker import Marker


@dataclass
class Genotype(Name):
    _markers: List[Marker]

    def __post_init__(self):
        super().__post_init__()
        self.__check_marker_list(self._markers)

    @property
    def markers(self):
        return self._markers

    @markers.setter
    def markers(self, markers: List[Marker]):
        self.__check_marker_list(markers)
        self._markers = markers

    @staticmethod
    def __check_marker_list(markers: List[Marker]) -> DataTypeError or None:
        if not isinstance(markers, list):
            raise DataTypeError
        if not all(isinstance(loc, Marker) for loc in markers):
            raise DataTypeError

    @staticmethod
    def _check_name(name: str) -> GenotypeNameError or None:
        if not isinstance(name, str):
            raise GenotypeNameError

    def to_dict(self):
        return {'name': self.name, 'markers': [marker.to_dict() for marker in self.markers]}
