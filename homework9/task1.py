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
    while len(all_numbers_from_files) > 0:
        min_num = min(
            list(
                enumerate(
                    ([int(numbers[0]) for numbers in all_numbers_from_files]), 0
                )
            ),
            key=lambda x: x[1],
        )
        sorted_numbers.append(min_num[1])
        all_numbers_from_files[min_num[0]].remove(str(min_num[1]))
        if len(all_numbers_from_files[min_num[0]]) == 0:
            all_numbers_from_files.remove(all_numbers_from_files[min_num[0]])

    return iter(sorted_numbers)
