
user_word = str(input("please enter user word here:"))

user_word = user_word.upper()

print("The uneaten letters in the word are")
for letter in user_word:
    if letter in "A" "E" "I" "O" "U":
        continue
    print(letter)
print("This ends here")