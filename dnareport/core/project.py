from dataclasses import dataclass, field
from typing import List, Tuple, Dict

from dnareport.core.base import Name
from dnareport.core.errors import ObjectListTypeError, GenotypeTypeError
from dnareport.core.genotype import Genotype


@dataclass
class Project(Name):
    _genotypes: List[Genotype] = field(default_factory=list, init=False)
    object_list: Tuple[str] or None = None
    __objects: Tuple[str] or None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        self.objects = self.object_list

    @property
    def genotypes(self) -> List[str]:
        return [genotype.name for genotype in self._genotypes]

    @property
    def objects(self) -> Tuple[str]:
        return self.__objects

    @objects.setter
    def objects(self, objects: Tuple[str]) -> None:
        self.__check_object_list(objects)
        self.__objects = objects

    @staticmethod
    def __check_object_list(objects: Tuple[str]) -> Exception or None:
        if objects is not None:
            if not isinstance(objects, tuple):
                raise ObjectListTypeError(objects)
            if not all(isinstance(obj, str) for obj in objects):
                raise ObjectListTypeError(objects)

    @staticmethod
    def __check_genotype(genotype) -> Exception or None:
        if not isinstance(genotype, Genotype):
            raise GenotypeTypeError(genotype)

    def __get_by_name(self, name: str) -> Genotype:
        for genotype in self._genotypes:
            if genotype.name == name:
                return genotype

    def __add_genotype(self, genotype: Genotype) -> None:
        current_genotype = self.__get_by_name(genotype.name)
        if current_genotype:
            current_genotype.add_marker(*genotype.markers)
        else:
            self._genotypes.append(genotype)

    def __filter(self, genotype: Genotype) -> None:
        if genotype.name in self.__objects:
            self.__add_genotype(genotype)

    def add_genotype(self, genotype: Genotype) -> None:
        self.__check_genotype(genotype)
        if self.__objects:
            self.__filter(genotype)
        else:
            self.__add_genotype(genotype)

    def __getitem__(self, key):
        return self.__get_by_name(str(key))

    def to_dict(self) -> Dict:
        return {'name': self.name, 'genotypes': [genotype.to_dict() for genotype in self._genotypes]}
