"""
In previous homework task 4, you wrote a cache function that remembers other
function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')
        # careful with input() in python2, use raw_input() instead

    >>> f()
    ? 1
    '1'
    >>> f()     # will remember previous value
    '1'
    >>> f()     # but use it up to two times only
    '1'
    >>> f()
    ? 2
    '2'
"""
from typing import Callable


def wrapper_cache(times: int):
    def cache(func: Callable) -> Callable:
        saved_data = {}
        times_call_func = {}

        def compute(*args):
            if args not in times_call_func:
                times_call_func[args] = 0
            if args in saved_data and times_call_func[args] < times:
                times_call_func[args] += 1
                return saved_data[args]
            else:
                times_call_func[args] = 0
                val_func = func(*args)
                saved_data.update([(args, val_func)])
                return val_func

        return compute

    return cache
