# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

import json
import mydictionary

my_dictionary_imported = mydictionary.mydictionary

# print(my_dictionary_imported)
print(my_dictionary_imported.get('recipes')[10])
print('################################################')
print(my_dictionary_imported.get('recipes')[10].get('ingredients'))
print('################################################')
print(my_dictionary_imported.get('recipes')[10].get('ingredients')[7])
