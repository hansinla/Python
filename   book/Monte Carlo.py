import random as random_number
import time


def MC(num_experiments, num_dice, num_sixes):
    succesful_events = 0

    for i in range(num_experiments):
        six = 0
        for j in range(num_dice):
            r = random_number.randint(1, 6)
            if r == 6:
                six += 1
        # successful event?
        if six >= num_sixes:
            succesful_events += 1

    p = float(succesful_events)/num_experiments

    return p

start_time = time.clock()
result  = MC(1000000, 2, 2)
end_time = time.clock()

print("Probability; ", result)
print("Time: ", end_time - start_time)
