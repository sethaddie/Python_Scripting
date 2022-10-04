

from tkinter.messagebox import NO


def fib_num(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2=1
    the_sum=0

    for i in range(3, n+1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum

    return the_sum

for n in range (1,10):
    print(n,"->", fib_num(n))

######################################################################################################################################

def fib_num(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    return fib_num(n-1)+ fib_num(n-2)

print(end="\n")

for n in range( 1, 20):
    print(n,"->", fib_num(n))