from dnareport.handler import Handler
from dnareport.loader import Loader


class DNAReportHandler:
    def __int__(self, path: str, ignore_merge_error: bool = False, objects: tuple or None = None):
        file, filename = Loader.load_report(path)
        self.__objects = objects
        self.report = Handler.handle(file, filename, ignore_merge_error, self.__objects)
