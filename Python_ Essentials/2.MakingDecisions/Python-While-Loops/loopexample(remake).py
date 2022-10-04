#from lib2to3.pytree import LeafPattern


number=int(input("Enter 0 to end program or value of number here:"))

largerst_number = 25

while number != 0:
    if number > largerst_number:
        largerst_number = number
    else:
        number=int(input("Enter 0 to end program or value of number here:"))

print("largest number is:", largerst_number)