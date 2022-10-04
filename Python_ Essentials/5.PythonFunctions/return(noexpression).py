def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    
    print("Happy New Year!")

#Providing False as an argument will modify the functions behavior
#The return instruction will cause its termination just before the wishes

happy_new_year(False)


