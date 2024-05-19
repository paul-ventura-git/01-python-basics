
name = input("What is your name? ")

print(f"Welcome, {name}")
print(type(name))

age = int(input("How old are you? ")) # int() converts the input to an integer
print(f"Nice age, {age}")
print(type(age))

weight = float(input("What is your weight in kilograms? "))
print(f"Nice weight, {weight}")
print(type(weight))

user_colors = input("Enter some of your favourite colors separated by commas: ")
colors = [s.strip() for s in user_colors.split(",")]

print(f"List of colors: {colors}")