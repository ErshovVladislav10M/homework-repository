"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import heapq
from contextlib import ExitStack
from typing import Iterator


def merge_sorted_files(file_list) -> Iterator:
    with ExitStack() as stack:
        files = [
            stack.enter_context(open(file_name)) for file_name in file_list
        ]
        return iter(
            [
                int(num.split()[0])
                for num in heapq.merge(*files, key=lambda x: int(x.split()[0]))
            ]
        )
