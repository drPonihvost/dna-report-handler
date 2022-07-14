from typing import List, Dict, Tuple

from dnareport.core.allele import Allele
from dnareport.core.genotype import Genotype
from dnareport.core.marker import Marker
from dnareport.core.project import Project
from dnareport.settings import Settings


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
    def __set_fields(header: List[str]) -> Dict:
        return {key: header.index(key) for key in Settings.REQUIRED_KEYS if key in header}

    @staticmethod
    def __read_alleles(fields: Dict, row: List[str]) -> List[Allele]:
        return [Allele(row[fields[f"Allele {i}"]]) for i in range(1, Settings.ALLELE_COUNT + 1)]

    @staticmethod
    def __read_marker(fields: Dict, row: List[str], ignore_merge_error) -> Marker:
        return Marker(row[fields['Marker']], ignore_merge_error)

    @staticmethod
    def __read_genotype(fields: Dict, row: List[str]) -> Genotype:
        return Genotype(row[fields['Sample Name']])

    @classmethod
    def __create_object(cls, fields: Dict, data: List[str], filename: str, objects: Tuple or None, ignore_merge_error: bool) -> Project:
        project = Project(filename, object_list=objects)
        for row in data:
            row = cls.__line_to_array(row)
            alleles = cls.__read_alleles(fields, row)
            marker = cls.__read_marker(fields, row, ignore_merge_error)
            marker.merge(alleles)
            genotype = cls.__read_genotype(fields, row)
            genotype.add_marker(marker)
            project.add_genotype(genotype)
        return project

    @classmethod
    def handle(cls, header, rest, filename: str, ignore_merge_error: bool, objects: tuple or None) -> Project:
        cls.__validate_fields(cls.__line_to_array(header))
        fields = cls.__set_fields(cls.__line_to_array(header))
        return cls.__create_object(fields, rest, filename, objects, ignore_merge_error)
