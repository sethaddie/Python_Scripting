
def addie_agg(lst):
    sum = 0

    for elem in lst:
        sum+=elem

    return sum
######################################################################################################################
print(addie_agg([10,23,71,32]))

def greetings(addie_list):

    for name in addie_list:
        print("Hi", name)

greetings(["bruh", "migga","bail"])
#######################################################################################################################
def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem**=2
        upd_list.append(elem)
    return upd_list

foo =[1,2,3,4,5]
print(list_updater(foo))