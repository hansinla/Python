# event handler.py

#----- define the event handler routines ---------------------
def handle_A():
    print ("Wrong! Try again!")

def handle_B():
    print("Absolutely right! Trillium is a kind of flower!")

def handle_C():
    print("Wrong! Try again!")

# ------------ define the appearance of the screen ------------
print ("\n"*100) # clear the screen
print (" VERY CHALLENGING GUESSING GAME")
print ("========================================================")
print ("Press the letter of your answer, then the ENTER key.")
print()
print ("    A. Animal")
print ("    B. Vegetable")
print ("    C. Mineral")
print()
print ("    X. Exit")
print()
print ("========================================================")
print ("What kind of thing is Trillium?")
print()


# ------------ event loop ------------
while 1:
    answer = input().upper()

    # key events
    if answer == "A":
        handle_A()
    elif answer == "B":
        handle_B()
    elif answer == "C":
        handle_C()
    if answer == "X":
        # clear the screen and exit the event loop
        print("\n"*100)
        break
