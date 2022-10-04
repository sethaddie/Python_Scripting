def my_function():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)


#A variable existing outside a function has a scope inside the functions' bodies, 
#excluding those of them which define a variable of the same name.

#It also means that the scope of a variable existing outside a function is supported only when getting its value (reading). 
#Assigning a value forces the creation of the function's own variable.





################################################################################################

#There's a special Python method which can extend a variable's scope 
#in a way which includes the functions' bodies #(even if you want not only to read the values, 
#but also to modify them).

def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

#Using this keyword inside a function with the name (or names separated with commas) of a variable(s), 
#forces Python to refrain from creating a new variable inside the function
#the one accessible from outside will be used instead.

