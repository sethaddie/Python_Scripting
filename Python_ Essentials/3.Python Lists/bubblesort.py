my_List=[52,100,63,32,41]
swapped = True

while swapped:
    swapped = False
    for i in range(len(my_List) - 1 ):
        if my_List[i] > my_List[i + 1]:
            swapped = True
            my_List[i], my_List[i + 1] = my_List[i + 1], my_List[i]
print(my_List)