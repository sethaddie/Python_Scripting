beatles=[]
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2", beatles)

#beatles=['John Lennon', 'Paul McCartney', 'George Harrison']
ask=int(input("How many name would you like to add:"))

for i in range(ask):
    name=input("Enter names of the beatle members:")
    beatles.append(name)
print("Step 3", beatles)

del beatles[4]
del beatles[3]

print("Step 4", beatles)

beatles.insert(0,'Bruh')
print("Step 5", beatles)


print("The Fab", len(beatles))
