addie_list = [1,2,3,4,5,6,7,8,9,10]
to_find = 5
found  = False

for i in range (len(addie_list)):
    found = addie_list[i] == to_find
    if found:
        break

if found:
    print("THe element found at index:",i)
else:
    print("absent")