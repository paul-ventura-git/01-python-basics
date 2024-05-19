thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Referring to the index with FOR
thislist = ["00", "01", "02"]
for i in range(len(thislist)):
  print(thislist[i])

# Referring to the index with WHILE
thislist = ["Paul", "Michael", "Redner"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# List Comprehension offers the shortest syntax for looping through lists:
# newlist = [expression 'for' item 'in' iterable (i.e. list) 'if' condition == 'True']
thislist = ["first", "second", "third"]
[print(x) for x in thislist]

# Copying elements from one list to other with condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# List Comprehension: Same example, shorter syntax.
fruits_2 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist_2 = [x for x in fruits if "a" in x]

print(newlist_2)