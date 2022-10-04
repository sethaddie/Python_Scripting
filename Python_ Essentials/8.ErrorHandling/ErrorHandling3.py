
#You can also specify and handle multiple built-in exceptions within a single except clause:
while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Wrong value or I cannot divide by zero")
    except:
        print("I don't know what to do...")