from lib2to3.pytree import LeafPattern


largest_number = 30
counter = 0

while True:
    number=int(input("Please enter zero to end program or value of the number here:"))
    if number == 0:
        break
    counter +=1
    if number > largest_number:
        largest_number = number
if counter !=0:
    print("The largest number is", largest_number)
else:
    print("You have not enter any number")  