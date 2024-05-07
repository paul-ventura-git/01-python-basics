# Placeholders

price_1 = 59
txt_1 = f"The price is {price_1} dollars"
print(txt_1)

# Display the price with two decimals

price_2 = 59
txt_2 = f"The price is {price_2:.2f} dollars"
print(txt_2)

# Perform operations on f-strings

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

# if statements

price_3 = 49
txt_3 = f"It is very {'Expensive' if price_3>50 else 'Cheap'}"

print(txt_3)

# execute functions

def myconverter(x):
  return x * 0.3048

txt_4 = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt_4)