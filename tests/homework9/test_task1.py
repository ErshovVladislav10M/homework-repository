import os

from homework9.task1 import merge_sorted_files


def test_merge_sorted_files():
    fi = open(os.getcwd() + "/file1.txt", "w")
    fi.write("1\n3\n5\n")
    fi.close()
    fi = open(os.getcwd() + "/file2.txt", "w")
    fi.write("2\n4\n6\n")
    fi.close()

    numbers = merge_sorted_files(["file1.txt", "file2.txt"])
    assert [1, 2, 3, 4, 5, 6] == [num for num in numbers]

    os.remove(os.getcwd() + "/file1.txt")
    os.remove(os.getcwd() + "/file2.txt")
