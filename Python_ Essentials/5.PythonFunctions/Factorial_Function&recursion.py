from itertools import product
from math import prod
import re


def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product=1

    for i in range(2,n+1):
        product *=i
    return product
    

for n in range(1, 7):
    print(n,factorial_function(n))


#########################################################################################################################################

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

print(end="\n")

for n in range(1,10):
    print(n,factorial_function(n))