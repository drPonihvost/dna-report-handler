from dataclasses import dataclass
from typing import List

from dnareport.core.allele import Allele
from dnareport.core.base import Name
from dnareport.core.errors import LocusNameError, DataTypeError


@dataclass
class Marker(Name):
    _alleles: List[Allele]

    def __post_init__(self):
        super().__post_init__()
        self.__check_allele_list(self._alleles)

    @property
    def alleles(self) -> List[Allele]:
        return self._alleles

    @alleles.setter
    def alleles(self, alleles: List[Allele]) -> None:
        self.__check_allele_list(alleles)
        self._alleles = alleles

    @staticmethod
    def _check_name(name: str) -> LocusNameError or None:
        if not isinstance(name, str):
            raise LocusNameError

    @staticmethod
    def __check_allele_list(alleles: List[Allele]) -> DataTypeError or None:
        if not isinstance(alleles, list):
            raise DataTypeError
        if not all(isinstance(allele, Allele) for allele in alleles):
            raise DataTypeError

    def to_dict(self):
        return {'name': self.name, 'alleles': [allele.to_dict() for allele in self.alleles]}
