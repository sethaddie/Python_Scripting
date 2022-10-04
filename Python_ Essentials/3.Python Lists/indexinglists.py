numbers = [13,45,67,48,46]
print("list of numbers:", numbers)

numbers[0] = 123
print("New list of numbers is:", numbers) 

numbers[3] = numbers[4] 

print("Current list of numbers:", numbers)

print("The length of the list is",len(numbers))

del numbers[2]


print("The updated list of numbers is:", numbers)
print("The current length of numbers is:", len(numbers))

#numbers.append(124)
#print("The updated list of numbers is:", numbers)