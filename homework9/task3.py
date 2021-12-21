"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import tokenize
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    counter = 0
    if tokenizer:
        for file in dir_path.glob(file_extension):
            with open(file, "rb") as fi:
                counter += sum(
                    1
                    for token in tokenize.tokenize(fi.readline)
                    if token.exact_type == 4
                )
    else:
        for file in dir_path.glob(file_extension):
            with open(file) as fi:
                counter += sum(1 for _ in fi)
    return counter
