def is_a_triangle(a,b,c):
    return a + b > c and b + c > a and c + a > b

a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a,b,c):
    print("Yes It can be a Triangle Fool")
else:
    print("Naah, It cant be a Triangle My G")