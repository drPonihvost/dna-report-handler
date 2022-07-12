from dataclasses import dataclass
from typing import List

from dnareport.core.allele import Allele
from dnareport.core.base import Name
from dnareport.core.errors import ReportNameError, DataTypeError
from dnareport.core.genotype import Genotype
from dnareport.core.marker import Marker


@dataclass
class DNAReport(Name):
    _genotypes: List[Genotype]

    def __post_init__(self):
        super().__post_init__()
        self.__check_genotype_list(self._genotypes)

    @property
    def genotypes(self) -> list:
        return self._genotypes

    @genotypes.setter
    def genotypes(self, genotypes: List[Genotype]) -> None:
        self.__check_genotype_list(genotypes)
        self._genotypes = genotypes

    @staticmethod
    def __check_genotype_list(genotypes: List[Genotype]) -> DataTypeError or None:
        if not isinstance(genotypes, list):
            raise DataTypeError
        if not all(isinstance(genotype, Genotype) for genotype in genotypes):
            raise DataTypeError

    @staticmethod
    def _check_name(name):
        if not isinstance(name, str):
            raise ReportNameError

    def to_dict(self):
        return {'name': self.name, 'genotypes': [genotype.to_dict() for genotype in self.genotypes]}


a1 = Allele('Allele 1', '15')
a2 = Allele('Allele 2', '17')
a3 = Allele('Allele 1', '9')
a4 = Allele('Allele 2', '9.3')

m1 = Marker('D3S1358', [a1, a2])
m2 = Marker('TH01', [a3, a4])

g = Genotype('123-1', [m1, m2])

r = DNAReport('2022-07-06-12', [g])
print(r.to_dict())
