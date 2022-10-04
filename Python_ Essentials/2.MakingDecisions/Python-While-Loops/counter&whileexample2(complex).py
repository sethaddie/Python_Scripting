largest_number = 30
counter = 0

number = int(input("Enter zero to end program or the value of number here:"))

while number != 0:
    if number == 0:
        continue
    counter +=1

    if number > largest_number:
        largest_number = number

    number = int(input("Enter zero to end program or the value of number here"))

if counter:
    print("The largest number is", largest_number)
else:
    print("You havent entered any number")