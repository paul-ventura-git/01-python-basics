import mydictionary

mydictionary = mydictionary.mydictionary

# print(mydictionary.get('recipes')[10])

# print(mydictionary.get('recipes')[0:])
mylistofrecipies = mydictionary.get('recipes')
servingsfour = []

for x in range(len(mylistofrecipies)):
  if mylistofrecipies[x]['servings']==4:
    servingsfour.append(mylistofrecipies[x])

print(servingsfour)
