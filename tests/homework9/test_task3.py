from pathlib import Path

from homework9.task3 import universal_file_counter


def test_universal_file_counter_without_tokenizer():
    fi = open(
        Path.cwd().parent
        / "homework-repository"
        / "tests"
        / "homework9"
        / "file1.txt",
        "w",
    )
    fi.write("1\n3\n5\n")
    fi.close()
    fi = open(
        Path.cwd().parent
        / "homework-repository"
        / "tests"
        / "homework9"
        / "file2.txt",
        "w",
    )
    fi.write("2\n4\n6\n")
    fi.close()

    Path.mkdir(
        Path.cwd().parent
        / "homework-repository"
        / "tests"
        / "homework9"
        / "ddd"
    )
    fi = open(
        Path.cwd().parent
        / "homework-repository"
        / "tests"
        / "homework9"
        / "ddd"
        / "file2.txt",
        "w",
    )
    fi.write("2\n4\n6\n")
    fi.close()

    lines = universal_file_counter(
        Path.cwd().parent / "homework-repository" / "tests" / "homework9",
        "*.txt",
    )
    assert lines == 9

    Path.unlink(
        Path.cwd().parent
        / "homework-repository"
        / "tests"
        / "homework9"
        / "file1.txt"
    )
    Path.unlink(
        Path.cwd().parent
        / "homework-repository"
        / "tests"
        / "homework9"
        / "file2.txt"
    )
    Path.unlink(
        Path.cwd().parent
        / "homework-repository"
        / "tests"
        / "homework9"
        / "ddd"
        / "file2.txt"
    )
    Path.rmdir(
        Path.cwd().parent
        / "homework-repository"
        / "tests"
        / "homework9"
        / "ddd"
    )


def test_universal_file_counter_with_tokenizer():
    fi = open(
        Path.cwd().parent
        / "homework-repository"
        / "tests"
        / "homework9"
        / "file1.txt",
        "w",
    )
    fi.write("1\n3\n5\n")
    fi.close()
    fi = open(
        Path.cwd().parent
        / "homework-repository"
        / "tests"
        / "homework9"
        / "file2.txt",
        "w",
    )
    fi.write("2\n4\n6\n")
    fi.close()

    lines = universal_file_counter(
        Path.cwd().parent / "homework-repository" / "tests" / "homework9",
        "*.txt",
        str.split,
    )
    assert lines == 6

    Path.unlink(
        Path.cwd().parent
        / "homework-repository"
        / "tests"
        / "homework9"
        / "file1.txt"
    )
    Path.unlink(
        Path.cwd().parent
        / "homework-repository"
        / "tests"
        / "homework9"
        / "file2.txt"
    )
