"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


class Suppressor:
    def __init__(self, exception):
        self.exception = exception

    @staticmethod
    def __enter__():
        pass

    def __exit__(self, exception, *args):
        return exception == self.exception


@contextmanager
def suppressor(exception):
    try:
        yield
    except exception:
        pass
