from typing import TextIO, List, Dict

from dnareport.core.allele import Allele
from dnareport.core.marker import Marker
from dnareport.core.report import DNAReport
from dnareport.core.settings import Settings


class Handler:
    @staticmethod
    def __line_to_array(line: str) -> List[str]:
        return line.split('\t')

    @staticmethod
    def __validate_fields(header: List[str]):
        for i in Settings.REQUIRED_KEYS:
            if header.count(i) == 0:
                raise KeyError

    @staticmethod
    def __set_fields(header: List[str]) -> Dict[str: int]:
        return {key: header.index(key) for key in Settings.REQUIRED_KEYS if key in header}

    @staticmethod
    def __read_alleles(field: Dict[str: int], row: List[str]) -> List[Allele]:
        alleles = []
        for i in range(1, Settings.ALLELE_COUNT + 1):
            key_in, key_out = f"Allele {i + 1}", f"allele_{i + 1}"
            if key_in in field and row[field[key_in]]:
                alleles.append(Allele(key_out, row[field[key_in]]))
        return alleles

    @staticmethod
    def __read_marker(field: Dict[str: int], row: List[str]):
        return Marker(row[field['Marker']])

    @classmethod
    def __create_object(cls, field: Dict[str: int], data: List[str]) -> DNAReport:
        for row in data:
            row = cls.__line_to_array(row)
            marker = cls.__read_marker(field, row)
            marker.alleles = cls.__read_alleles(field, row)

            genotype =


    @classmethod
    def handle(cls, file: TextIO, filename: str, ignore_merge_error: bool, objects: tuple or None):
        header, *rest = file.read().splitlines()
        cls.__validate_fields(cls.__line_to_array(header))
        fields = cls.__set_fields(header)
        return cls.__create_object()

