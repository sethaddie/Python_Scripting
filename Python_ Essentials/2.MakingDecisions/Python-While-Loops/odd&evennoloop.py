number=int(input("Enter 0 to stop thr program or value of number here:"))

odd_numbers = 0
even_numbers = 0

while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    number=int(input("Enter 0  to stop the program or value of number here:"))

print("odd numbers count is;", odd_numbers)
print("even numbers count is:", even_numbers)
        