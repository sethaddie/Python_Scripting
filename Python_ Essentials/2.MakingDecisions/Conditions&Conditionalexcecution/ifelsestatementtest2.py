income = float(input("Enter the annual income: "))

if income <=85528:
    if 0.18*income <= 557:
        tax = 0.0
    else:
        tax = (0.18*income - 556.2)
           
else:
    tax = (14839.2+(0.32*(income-85528)))

     

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
