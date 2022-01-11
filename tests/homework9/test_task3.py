import os
from pathlib import Path

from homework9.task3 import universal_file_counter


def test_universal_file_counter_without_tokenizer():
    fi = open(os.getcwd() + "/file1.txt", "w")
    fi.write("1\n3\n5\n")
    fi.close()
    fi = open(os.getcwd() + "/file2.txt", "w")
    fi.write("2\n4\n6\n")
    fi.close()

    lines = universal_file_counter(Path.cwd(), "*.txt")
    assert lines == 6

    os.remove(os.getcwd() + "/file1.txt")
    os.remove(os.getcwd() + "/file2.txt")


def test_universal_file_counter_with_tokenizer():
    fi = open(os.getcwd() + "/file1.txt", "w")
    fi.write("1\n3\n5\n")
    fi.close()
    fi = open(os.getcwd() + "/file2.txt", "w")
    fi.write("2\n4\n6\n")
    fi.close()

    lines = universal_file_counter(Path.cwd(), "*.txt", str.split)
    assert lines == 6

    os.remove(os.getcwd() + "/file1.txt")
    os.remove(os.getcwd() + "/file2.txt")
