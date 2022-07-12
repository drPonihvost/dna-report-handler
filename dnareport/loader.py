import os
from typing import TextIO

from dnareport.core.settings import Settings


class Loader:
    @staticmethod
    def __check_path(path):
        if not isinstance(path, str):
            raise TypeError('Значение должно иметь тип str')

    @classmethod
    def load_report(cls, path: str):
        return cls.__open_file(path)

    @classmethod
    def __open_file(cls, path: str) -> TextIO and str:
        cls.__check_path(path)
        try:
            with open(path, 'r') as file:
                filename, ext = os.path.splitext(os.path.basename(file.name))
                if ext not in Settings.EXT:
                    raise ValueError(f"Неподдерживаемое расширение {ext}")
                return file, filename
        except OSError:
            raise OSError('Некорректный файл')


# report = DNAReportHandler('/home/philipp/PycharmProjects/PyPi/dna-report-handler/README.md')
report = Loader.load_report('/home/philipp/PycharmProjects/PyPi/dna-report-handler/requirements_dev.txt')
