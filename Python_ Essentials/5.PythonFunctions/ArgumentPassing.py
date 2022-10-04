#Positional argument passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
    
introduction("Seth", "Addie")

#Keyword argument passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(last_name="Addie", first_name="Seth")