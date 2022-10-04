from audioop import add
from tkinter.tix import DirSelectDialog


addie_dictionary={
                  "cat":"chat",
                  "dog":"chien",
                  "horse":"cheval"
                  }
#USING FOR LOOPS key() method

for key in addie_dictionary.keys():
    print(key, "->", addie_dictionary[key])

#USING FOR LOOPS Items() method

for english, french in addie_dictionary.items():
    print(english, "->", french)

#USING FOR LOOPS Value() method

for french in addie_dictionary.values():
    print(french)

#for keys in addie_dictionary.keys():
#   print(keys)

#THE SORTED FUNCTION

for keys in sorted(addie_dictionary.keys()):
    print(keys)


#MODIFYING AND ADDING VALUES

addie_dictionary["cat"] = "minou"
print(addie_dictionary)

#ADDING A NEW KEY
addie_dictionary['swan'] = "cygne"
print(addie_dictionary)

#OR

addie_dictionary.update({"duck":"canard"})
print(addie_dictionary)

#REMOVING A KEY
del addie_dictionary["dog"]
print(addie_dictionary)

#REMOVING LAST ITEM OF DICTIONARY
addie_dictionary.popitem()
print(addie_dictionary)