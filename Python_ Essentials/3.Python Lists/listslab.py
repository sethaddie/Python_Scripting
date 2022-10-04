hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

replace_midno=int(input("Enter number to replace the midle number:"))
hat_list[2] = replace_midno

del hat_list[-1]

print("The length of the list is", len(hat_list))

print("The hat_list is",hat_list)