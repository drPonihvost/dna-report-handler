class AlleleValueError(Exception):
    pass


class LocusNameError(ValueError):
    pass


class GenotypeNameError(ValueError):
    pass


class ReportNameError(ValueError):
    pass


class DataTypeError(Exception):
    def __init__(self, message, value):
        super().__init__(message)
        self.value = value

    def __str__(self):
        return


class MergeError(ValueError):
    pass
