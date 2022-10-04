#Imagine a list - not very long, not very complicated, just a simple list containing some integer numbers. 
#Some of these numbers may be repeated, and this is the clue. 
#We don't want any repetitions. We want them to be removed.
#addie_list=[1,2,4,4,1,4,2,6,2,9] 

from audioop import add


addie_list=[1,2,4,4,1,4,2,6,2,9] 
addie_new_list=[]

for number in addie_list:
    if number not in addie_new_list:
        addie_new_list.append(number)

addie_list = addie_new_list
print("The list with the unique elements only is :", addie_list)