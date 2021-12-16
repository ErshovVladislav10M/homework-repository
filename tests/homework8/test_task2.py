import os

from homework8.task2 import TableData


def test_table_data_len():
    presidents = TableData(
        os.getcwd() + "/homework8/" + "test_data_task2.sqlite", "presidents"
    )
    assert len(presidents) == 3


def test_table_data_contains():
    presidents = TableData(
        os.getcwd() + "/homework8/" + "test_data_task2.sqlite", "presidents"
    )
    assert "Trump" in presidents


def test_table_data_iterable():
    presidents = TableData(
        os.getcwd() + "/homework8/" + "test_data_task2.sqlite", "presidents"
    )
    assert [president[0] for president in presidents] == [
        "Yeltsin",
        "Trump",
        "Big Man Tyrone",
    ]
