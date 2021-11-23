import os
import sys

from homework4.task_3_get_print_output import my_precious_logger


def test_positive():
    my_precious_logger("OK")
    assert open(os.getcwd() + "/stdout_text.txt", "r").read() == "OK"


def test_negative():
    my_precious_logger("error: file not found")
    assert sys.stderr == "error: file not found"
