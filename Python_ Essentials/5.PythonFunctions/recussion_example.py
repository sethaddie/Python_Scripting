

from shutil import register_unpack_format


def factorial(n):
    if n == 1: #base termination condition.
        return 1
    else:
        return n * factorial(n-1)

