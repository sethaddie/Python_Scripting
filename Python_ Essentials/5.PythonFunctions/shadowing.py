def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)

#A situation like this activates a mechanism called shadowing:
#parameter x shadows any variable of the same name, but...
#... only inside the function defining the parameter.
#The parameter named number is a completely different entity from the variable named number.