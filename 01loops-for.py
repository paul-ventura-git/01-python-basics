cars = ["audi", "chevrolet", "ford", "lexus"]

# Print all the elements in the LIST
print("******************** for x in cars:")
for x in cars:
    print(x)

# Print all the elements in the STRING
print("******************** for y in 'banana':")
for y in "banana":
    print(y)

# Print all the elements in the STRING until 'cherry' is found
print("******************** for z in fruits: if z == 'cherry': continue")
fruits = ["apple", "banana", "cherry"]
for z in fruits:
    if z == "cherry":
        continue
    print(z)

print("#############################")
for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")