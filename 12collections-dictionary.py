# Duplicates are not allowed
# Elements can be of any data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(len(thisdict))
print(thisdict["brand"])
print(type(thisdict))
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items()) # Return the values as tuples

thisdict_2 = dict(name = "John", age = 36, country = "Norway")
print(thisdict_2)