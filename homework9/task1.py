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
from typing import Iterator


def merge_sorted_files(file_list) -> Iterator:
    all_numbers_from_files = []
    for file_name in file_list:
        with open(file_name) as fi:
            all_numbers_from_files.append(fi.read().split())

    sorted_numbers = []
    for j in range(len(all_numbers_from_files[0])):
        for i in range(len(all_numbers_from_files)):
            sorted_numbers.append(int(all_numbers_from_files[i][j]))

    return iter(sorted_numbers)
