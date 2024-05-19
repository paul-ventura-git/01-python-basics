# Python3 program introducing f-string

name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")

# Prints today's date with help
# of datetime library
import datetime
 
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")


amount = 150.75
print("Amount: ${:.2f}".format(amount))