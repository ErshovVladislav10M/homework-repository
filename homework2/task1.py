"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    ans_words = ["" for i in range(10)]
    len_words = [0 for i in range(10)]
    with open(file_path) as fi:
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
    ...


def count_punctuation_chars(file_path: str) -> int:
    """I count ascii characters with codes from 33 to 47"""
    counter = 0
    with open(file_path + ".txt") as fi:
        for line in fi:
            for i in line:
                if 48 > ord(i) > 32:
                    counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...