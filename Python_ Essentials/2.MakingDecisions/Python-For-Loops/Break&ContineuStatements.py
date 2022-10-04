#break -example

print("The break Instruction")
for i in range (1,10):
    if i == 4:
        break
    print("Inside the loop", i)
print("Outside the loop")

#continue example

print("Contineu example")
print("The contineu instruction")

for i in range(1, 10):
    if i == 4:
        continue
    print("Inside the loop", i)
print("Outside the loop")