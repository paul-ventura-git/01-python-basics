# append()	Adds an element at the end of the list
# clear()	  Removes all the elements from the list
# copy()	  Returns a copy of the list
# count()	  Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	  Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	  Sorts the list

import mylist
import json

my_list_of_users = mylist.mylist

my_list_of_users.append("Something")
print(my_list_of_users)
print('##########################################################')
print(len(my_list_of_users))
print(my_list_of_users[3])
print('##########################################################')
my_list_of_users.reverse()
print(my_list_of_users)
print('##########################################################')
