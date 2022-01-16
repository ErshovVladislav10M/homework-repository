from pathlib import Path

from homework9.task1 import merge_sorted_files


def test_merge_sorted_files():
    fi = open(Path.cwd() / "file1.txt", "w")
    fi.write("3\n8\n15\n")
    fi.close()
    fi = open(Path.cwd() / "file2.txt", "w")
    fi.write("1\n2\n5\n")
    fi.close()

    numbers = merge_sorted_files(["file1.txt", "file2.txt"])
    assert [1, 2, 3, 5, 8, 15] == [num for num in numbers]

    Path.unlink(Path.cwd() / "file1.txt")
    Path.unlink(Path.cwd() / "file2.txt")
