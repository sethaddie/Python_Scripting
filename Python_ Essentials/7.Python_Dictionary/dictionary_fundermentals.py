dictionary = {"cat":"chat","dog":"chien", "horse":"chavel"}

phone_numbers = {"addie":790366587,"trap":74358903 }

empty_dictionary={}

words=['cat', 'lion', 'dog', 'horse']

print(dictionary)
print(phone_numbers)
print(phone_numbers["addie"])
print(empty_dictionary)

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word,"is not in dictionary")