import random

namesList = ["daniela", "julian", "hans", "daniela", "julian", "hans"]

while len(namesList) > 0:
    myChoice = random.choice(namesList)
    print(myChoice)
    idx = namesList.index(myChoice)
    namesList.pop(idx)
