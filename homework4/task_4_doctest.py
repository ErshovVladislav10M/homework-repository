"""
Write a function that takes a number N as an input
and returns N FizzBuzz numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15,
"Робот Фортран, чисть картошку!"
"""
import doctest
import math
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Return list with fizz, buzz and numbers

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    >>> fizzbuzz(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    """

    if n < 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")

    ans = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            ans.append("fizz")
        elif i % 5 == 0:
            ans.append("buzz")
        else:
            ans.append(str(i))
    return ans


if __name__ == "__main__":
    doctest.testmod()
