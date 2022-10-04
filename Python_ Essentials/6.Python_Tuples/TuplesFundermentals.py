
#CREATING TUPLES

tuple_1 = (1,2,4,8)
tuple_2 = 1., .5 , .25,.125

print(tuple_1)
print(tuple_2)

#HOW TO USE TUPLES

my_tuple = (1,10,100,1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for n in my_tuple:
    print(n)

#MORE WAYS TO MANIPULATE AND USE TUPLES

my_tupe_1=(1, 10, 100)
my_tupe_2= my_tupe_1 +(1000,10000)
my_tupe_3=my_tupe_1*3

print(len(my_tupe_3))
print(my_tupe_2)
print(my_tupe_3)
print(10 in my_tupe_1)
print(-10 not in my_tupe_1)

#SWAPPING EFFECT

var=123

my_tuple__1 = (1,)
my_tuple__2=(2,)
my_tuple__3=(3, var)

my_tuple__1, my_tuple__2, my_tuple__3 = my_tuple__2, my_tuple__3, my_tuple__1

print(my_tuple__1, my_tuple__2, my_tuple__3)
