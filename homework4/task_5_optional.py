"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach
for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator


def loop(base):
    yield base + 1
    yield base + 2
    yield "fizz"
    yield base + 4
    yield "buzz"
    yield "fizz"
    yield base + 7
    yield base + 8
    yield "fizz"
    yield "buzz"
    yield base + 11
    yield "fizz"
    yield base + 13
    yield base + 14
    yield "fizzbuzz"
    

def unlim_fizzbuzz():
    index = 0
    while True:
        for element in loop(base=index*15):
            yield element
        index += 1


def fizzbuzz(n: int):
    generator = unlim_fizzbuzz()
    for _ in range(n):
        yield next(generator)
