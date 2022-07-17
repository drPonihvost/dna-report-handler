import os
from typing import TextIO

from dnareport.core.errors import ExtensionError, OpenFileError
from dnareport.settings import Settings


class Loader:
    @staticmethod
    def __check_path(path):
        if not isinstance(path, str):
            raise TypeError(path)

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
                    raise ExtensionError(ext)
                header, *rest = file.read().splitlines()
                return header, rest, filename
        except OSError:
            raise OpenFileError(filename)
