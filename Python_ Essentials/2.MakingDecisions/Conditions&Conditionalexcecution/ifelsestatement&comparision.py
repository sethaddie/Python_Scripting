from turtle import numinput


number1=int(input("Please enter the value of the first number:"))
number2=int(input("Please enter the value of the second number:"))
number3=int(input("Please enter the value of the third number:"))

#assuming that number 1 is the largest number
largernumber=number1

#is number 2 greater than the larger number ???
if number2 > largernumber:
    largernumber = number2
#is number 3 greater than the larger number ???
if number3 > largernumber:
    largernumber = number3

print("The largernumber is:", largernumber)
