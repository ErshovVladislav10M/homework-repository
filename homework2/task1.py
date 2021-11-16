"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
import sys
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    ans_words = ["" for i in range(10)]
    len_words = [0 for i in range(10)]
    with open(file_path, encoding="unicode-escape") as fi:
        for line in fi:
            words = line.split()
            for word in words:
                set_letters = set(word)
                i_min_len = len_words.index(min(len_words))
                if len(set_letters) > len_words[i_min_len]:
                    ans_words[i_min_len] = word
                    len_words[i_min_len] = len(set_letters)
    return ans_words


def get_rarest_char(file_path: str) -> str:
    dict_letters = {}
    with open(file_path, encoding="unicode-escape") as fi:
        for line in fi:
            for letter in line:
                if dict_letters.get(letter, -1) == -1:
                    dict_letters.update([(letter, 1)])
                else:
                    dict_letters[letter] += 1

    minor_letter, minor_count = dict_letters.popitem()
    while len(dict_letters) > 0:
        letter, count = dict_letters.popitem()
        if count < minor_count:
            minor_letter = letter
            minor_count = count

    return minor_letter


def count_punctuation_chars(file_path: str) -> int:
    """I count ascii characters with codes from 33 to 47"""
    counter = 0
    with open(file_path, encoding="unicode-escape") as fi:
        for line in fi:
            for i in line:
                if 48 > ord(i) > 32:
                    counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    ans = 0
    with open(file_path, encoding="unicode-escape") as fi:
        for line in fi:
            for letter in line:
                if not letter.isascii():
                    ans += 1
    return ans


def get_most_common_non_ascii_char(file_path: str) -> str:
    """If there are no non-ascii characters in the file, SystemExit"""
    dict_letters = {}
    with open(file_path, encoding="unicode-escape") as fi:
        for line in fi:
            for letter in line:
                if dict_letters.get(letter, -1) == -1:
                    dict_letters.update([(letter, 1)])
                else:
                    dict_letters[letter] += 1

    major_letter = None
    major_count = -1
    while len(dict_letters) > 0:
        letter, count = dict_letters.popitem()
        if (
                count > major_count or major_count == -1
        ) and not letter.isascii():
            major_letter = letter
            major_count = count

    if not major_letter:
        sys.exit()
    return major_letter