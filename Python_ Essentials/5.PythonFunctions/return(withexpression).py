from audioop import mul
import re


def boring_function():
    return 123

x = boring_function()

print("Result for boring_function is",x)

#The return instruction, enriched with the expression (the expression is very simple here), 
# "transports" the expression's value to the place where the function has been invoked.


val1 = int(input("Enter val1:"))
val2 = int(input("Enter val2:"))
def multiply (val1,val2):
    product = val1 *val2
    add = val1 + val2

    if val1*val2 >= 100:
        return product
    else:
        return add


result = multiply(val1,val2)
print(result)