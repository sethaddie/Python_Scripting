
mylist=[65,62,76,23,84]

mylist[0], mylist[4] = mylist[4], mylist[0]
mylist[1], mylist[3] = mylist[3], mylist[1]

print(mylist)


#The method used below is able to swap the lists's indexes despite of its length.
mylist=[65,62,76,23,84]
length =len(mylist)

for i in range (length // 2):
    mylist[i], mylist[length-i-1] = mylist[length-i-1], mylist[i]
print(mylist) 