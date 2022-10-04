secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number=int(input("Enter your best guess for the number here:"))

while number != secret_number:
    print("Ha ha! You're stuck in my loop")
    number=int(input("Enter the number here again:"))

print("Well done, muggle! You're Free now.")