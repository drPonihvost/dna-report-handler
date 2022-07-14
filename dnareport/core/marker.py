from dataclasses import dataclass, field
from typing import List, Dict

from dnareport.core.allele import Allele
from dnareport.core.base import Name
from dnareport.core.errors import LocusNameError, DataTypeError, MergeError


@dataclass
class Marker(Name):
    ignore_merge_error: bool = False
    _alleles: List[Allele] = field(default_factory=list, init=False)

    def __post_init__(self) -> None:
        super().__post_init__()
        self.__check_ignore_error(self.ignore_merge_error)

    @property
    def alleles(self) -> List[Allele]:
        return self._alleles

    @staticmethod
    def _check_name(name: str) -> Exception or None:
        if not isinstance(name, str):
            raise LocusNameError

    @staticmethod
    def __check_allele(allele: Allele) -> Exception or None:
        if not isinstance(allele, Allele):
            raise DataTypeError

    @staticmethod
    def __check_allele_list(alleles: List[Allele] or List) -> Exception or None:
        if not isinstance(alleles, list):
            raise DataTypeError
        if not all(isinstance(allele, Allele) for allele in alleles):
            raise DataTypeError

    @staticmethod
    def __check_ignore_error(param: bool) -> Exception or None:
        if not isinstance(param, bool):
            raise DataTypeError

    def __check_for_compliance(self, other: List[Allele]) -> Exception or None:
        if self._alleles and other:
            if set(self._alleles) != set(other) and not self.ignore_merge_error:
                raise MergeError

    def __is_duplicate(self, allele: Allele) -> bool:
        return allele in self._alleles

    def __add_allele(self, allele: Allele) -> None:
        self.__check_allele(allele)
        if self._alleles:
            if self.__is_duplicate(allele) or not allele.value:
                return
        self._alleles.append(allele)

    def merge(self, other: List[Allele]) -> None:
        self.__check_allele_list(other)
        self.__check_for_compliance(other)
        for allele in other:
            self.__add_allele(allele)

    def to_dict(self) -> Dict:
        return {'name': self.name, 'alleles': sorted([allele.value for allele in self._alleles])}
