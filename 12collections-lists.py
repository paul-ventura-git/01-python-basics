thislist = ["0 apple", "1 banana", " 2 cherry", "3 apple", "4 cherry", True, 33]
print(thislist)
print(len(thislist))
print(type(thislist))
print(thislist[1])
print(thislist[-1])   # Negative indexing means start from the end
print(thislist[3:6])  # 3 included, 6 not
print(thislist[:4])   # 4 is not included
print(thislist[2:])   # 2 is included
print(thislist[-4:-1])

print("#####################################################")
otherlist = list(("bouganvillea", "daisy", "rose")) # note the double round-brackets
print(otherlist)


