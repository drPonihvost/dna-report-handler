from dnareport.handler import Handler
from dnareport.loader import Loader


class DNAReportHandler:
    def __init__(self, path: str, ignore_merge_error: bool = False, objects: tuple or None = None) -> None:
        header, rest, filename = Loader.load_report(path)
        self.report = Handler.handle(header, rest, filename, ignore_merge_error, objects)
