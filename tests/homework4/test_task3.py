import os
import sys
import pytest

from homework4.task_3_get_print_output import my_precious_logger


def test_positive(capfd):
    my_precious_logger("OK")
    out, err = capfd.readouterr()
    assert out == "OK\n"


def test_negative():
    my_precious_logger("error: file not found")
    assert sys.stderr == "error: file not found"
