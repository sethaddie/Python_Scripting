


addie_list=[21,7,4,14,5,11,17,6]
largest = addie_list[0]

for i in addie_list:
    if i > largest:
        largest = i
print(largest)


#The program above performs one unnecessary comparision, when the first
#element is compared with itself.


addie_list=[21,7,4,14,5,11,17,6]
largest = addie_list[0]

for i in addie_list[1:]:
    if i > largest:
        largest = i
print(largest)

#To save computer power, you can use a slice.