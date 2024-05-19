thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Referring to the index with FOR
thislist = ["00", "01", "02"]
for i in range(len(thislist)):
  print(thislist[i])

# Referring to the index with WHILE
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# List Comprehension offers the shortest syntax for looping through lists:
thislist = ["first", "second", "third"]
[print(x) for x in thislist]