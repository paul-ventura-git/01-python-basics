cars = ["audi", "chevrolet", "ford", "lexus"]

# Print all the elements in the LIST
print("******************** for x in cars:")
for x in cars:
    print(x)

# Print all the elements in the STRING
print("******************** for y in 'banana':")
for y in "banana":
    print(y)

# Print all the elements in the STRING until 'cherry' is found (BREAK)
print("******************** for z in fruits: if z == 'cherry': continue")
fruits = ["apple", "banana", "cherry"]
for z in fruits:
    if z == "cherry":
        continue
    print(z)

# "in range" have a sequence like the indexes of arrays (starting from zero)
# Print all the elements until number 6 (<6)
print("******************** for x in range(6):")
for x in range(6):
  print(x)

# Print all the elements from 2 (1) until number 6 (5)
print("******************** for x in range(2, 6):")
for x in range(2, 6):
  print(x)

# Print all the elements from 2 (1) until number 30 (29). Three by three
print("******************** for x in range(2, 30, 3):")
for x in range(2, 30, 3):
  print(x)

# Print all the elements and break when value is met
print("******************** for x in range(6): if x == 3: break")
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")