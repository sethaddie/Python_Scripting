name = str(input("Enter your name please:"))

name = name.upper()
length = len(name)
for i in range(length):
    for letter in name[i]:
        if letter not in ('A', 'E', 'I', 'O', 'U'):
            print(letter)
            continue