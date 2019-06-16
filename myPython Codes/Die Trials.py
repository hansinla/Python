import random

TRIALS = 1000000

sides = [0, 0, 0, 0, 0, 0 ]

for _ in range(TRIALS):
    sides[random.randrange(6)] += 1

for _ in range(6):
    print("Side ", _ ,": ",  sides[_], " probablity: ", sides[_]/TRIALS)
    
