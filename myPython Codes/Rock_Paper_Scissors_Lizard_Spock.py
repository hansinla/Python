# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def number_to_name(number):
    '''(number)->str
    '''
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        name = 'undefined'
    return name


def name_to_number(name):
    '''(str)->int
    '''
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print("The name",name,"is not defined.")
        number = -1
    return number



def rpsls(name):
    '''
    '''
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    random.seed()
    comp_number = random.randrange(5)
    # compute difference of player_number and comp_number modulo five
    dif = (player_number - comp_number)%5
    # use if/elif/else to determine winner
    if dif == 0:
        result = "Player and computer tie!"
    elif dif == 1 or dif == 2:
        result = "Player wins!"
    else:
        result = "Computer wins!"
    # print results
    print("Player chooses",name)
    print("Computer chooses",number_to_name(comp_number))
    print(result)
    print()



# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


