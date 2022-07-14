from dnareport.handler import Handler
from dnareport.loader import Loader


class DNAReportHandler:
    def __init__(self, path: str, ignore_merge_error: bool = False, objects: tuple or None = None):
        header, rest, filename = Loader.load_report(path)
        self.__objects = objects
        self.report = Handler.handle(header, rest, filename, ignore_merge_error, self.__objects)


if __name__ == '__main__':
    report = DNAReportHandler(path=r"C:\Users\Philipp\Desktop\PAFOS\Проекты\test_lib.txt", ignore_merge_error=True, objects=('167-1',))
    print(report.report.to_dict())
    print(report.report.genotypes[0])
