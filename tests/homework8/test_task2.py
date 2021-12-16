import os

from homework8.task2 import TableData


def test_table_data_len():
    presidents = TableData(
        os.getcwd() + "/homework8/" + "test_data_task2.sqlite", "presidents"
    )
    assert len(presidents) == 3
