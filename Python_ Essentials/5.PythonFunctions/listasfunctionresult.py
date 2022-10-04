
def strange_list_fun(n):
    strange_list = []

    for i in range (0, n):
        strange_list.insert(0, i)

    return strange_list
print(strange_list_fun(10))

#############################################################################################################################

def create_addie__list(n):
    addie_list=[]

    for i in range(n):
        addie_list.append(i)
    return addie_list

print(create_addie__list(15))

##############################################################################################################################

def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(even_num_lst(11))