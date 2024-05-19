import mylist

mylist = mylist.mylist

result=[]

# Returns all the objects that have a zipcode beginning with '5'
for x in range(len(mylist)):
  if mylist[x]['address']['zipcode'][0]=='5':
    result.append(mylist[x])

print(result)