# "Guess the number" mini-project
# If you're playing this in Safari on Mac OS X,
# make sure that you're not in Full Screen mode.
import simplegui
import random

# initialize global variables used in your code
number_of_guesses = 0
secret_number = 0
desired_range = 100
previous=[]

# Define "helper" functions
def start_new_game(desired_range):
    global previous
    previous=[]
    if desired_range == 100:
        range100()
    else:
        range1000()

def output():
    if number_of_guesses > 1:
        print "You have", number_of_guesses,"guesses remaining.\n"
    else:
        print "You have only one guess remaining. Make it count!\n"

def get_random_number(range):
    global secret_number
    secret_number = random.randrange(0, range)

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global number_of_guesses, desired_range
    number_of_guesses = 7
    desired_range = 100
    get_random_number(100)
    print "Let's play a game! Guess a number between 0 and",desired_range,"\n"
    output()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global number_of_guesses, desired_range
    number_of_guesses = 10
    desired_range = 1000
    get_random_number(1000)
    print "Let's play a game! Guess a number between 0 and",desired_range,"\n"
    output()
    
def get_input(guess):
    global number_of_guesses
    print "You guessed", guess
    if (int(guess) in previous):
        print "You tried",guess,"already. It's not correct."
    else:
        previous.append(int(guess))
    
    if int(guess) == secret_number:
        print "Correct! My secret number is:", secret_number
        return (start_new_game(desired_range))
    else:
        if number_of_guesses > 1:
            if int(guess) > secret_number:
                print "The secret number is lower!"
            else:
                print "The secret number is higher!"
        else:
            print "No that's not it either. Game over!\n"
            return (start_new_game(desired_range))
    number_of_guesses -= 1
    output()
   
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements
frame.add_button("Range: 0 - 100", range100, 150)
frame.add_button("Range: 0 - 1000", range1000, 150)
frame.add_input("Your guess:", get_input, 150)

# start frame & first game
frame.start()
start_new_game(desired_range)
