#changing the parameter's value doesn't propagate outside the function 
#(in any case, not when the variable is a scalar, like in the example).

#This also means that a function receives the argument's value, not the argument itself. This is true for scalars.

#(do you recall the peculiarities of assigning list slices versus assigning lists as a whole?).



def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

#######################################################################################################################################################
print(end="\n")

my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)