
def is_a_triangle(a,b,c):
    if a + b <= c or a + c <= b or c + b <= a :
        return False
    return True

a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

print(is_a_triangle(a,b,c))

#########################################################################################

