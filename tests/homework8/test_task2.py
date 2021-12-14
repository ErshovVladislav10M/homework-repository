import os

from homework8.task2 import TableData


def test_TableData():
    storage = TableData(
        os.getcwd() + "/homework8/" + "test_data_task2.sqlite"
    )
