import os

from homework4.task_1_read_file import read_magic_number


def test_positive():
    fi = open("test_task1_text.txt", "w")
    fi.write("2")
    fi.close()
    ans = read_magic_number(os.getcwd() + "/test_task1_text.txt")
    os.remove(os.getcwd() + "/test_task1_text.txt")
    assert ans == True
