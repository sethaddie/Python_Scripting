def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)

#changing the parameter's value doesn't propagate outside the function 
#(in any case, not when the variable is a scalar, like in the example).

#This also means that a function receives the argument's value, not the argument itself. This is true for scalars.