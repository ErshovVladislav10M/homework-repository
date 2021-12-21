from homework9.task2 import suppressor


def test_suppressor():
    with suppressor(IndexError):
        ...
