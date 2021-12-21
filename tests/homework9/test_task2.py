from homework9.task2 import Suppressor, suppressor


def test_suppressor():
    with suppressor(IndexError):
        ...


def test_Suppressor():
    with Suppressor(ValueError):
        ...
