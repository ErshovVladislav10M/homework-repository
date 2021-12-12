import os

from homework8.task1 import KeyValueStorage


def test_KeyValueStorage():
    storage = KeyValueStorage(
        os.getcwd() + "/homework8/" + "test_data_task1.txt"
    )
    assert storage["name"] == "kek"
    assert storage.name == "kek"
