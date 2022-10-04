from ast import Num


try:
    num=int(input("Enter value here:"))
    print("THe reciprical of", num, "->", 1/num)

except ValueError:
    print("I am stuck bruh")

except ZeroDivisionError:
    print("Division of zero is not allowed in our universe")

#default exceot branch
except:
    print("something strange happened here.... Sorry bruh")