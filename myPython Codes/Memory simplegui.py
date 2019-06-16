# implementation of card game - Memory
import simplegui
import random

# globals
moves = 0
match = False
first_index = 0
second_index = 0
WIDTH = 800
HEIGHT = 100
CARD_WIDTH = WIDTH/16

# helper function to initialize globals
def init():
    global state, card_list, flipped_list, moves
    # flipped_list is used to keep track of turned cards with booleans
    flipped_list = []
    # card_list is the playing deck
    card_list = range(8) * 2
    random.shuffle(card_list)
    for i in card_list:
         flipped_list.append(False)
    # setup initial state and reset number of moves
    state = 0
    moves = 0
    label.set_text("Moves = "+str(moves))
           
# define event handlers
def mouseclick(pos):
    global state, moves, first_index, second_index, match
    
    # get the index of the card clicked on
    idx = pos[0] // 50
    # clicking on a turned card doesn't do anything so check for that first
    if flipped_list[idx] == False: 
        if state == 1:
            state = 2
            second_index = idx	# store the card index in a variable
        else:
            state = 1
            # flip the previous two cards back if there's no match
            if  match == False:
                flipped_list[first_index] = False
                flipped_list[second_index] = False
            first_index = idx	# store the card index in a variable
        # if appropriate, increase moves counter
        if state == 1:
            moves += 1
            label.set_text("Moves = "+str(moves))
        else:
            # on the second card, check for match and store the result for the next click
            if card_list[first_index] == card_list[idx]:
                match = True
            else:
                match = False
        flipped_list[idx] = True
                        
# draw the cards by means of the two lists  
def draw(canvas):
    global card_list, flipped_list
    
    # use an index to loop and use it for drawing
    for idx in range (0, 16):
        offset = (idx * 50)
        if flipped_list[idx] == True:
            card_string = str(card_list[idx])
            text_pos = offset + 32 - frame.get_canvas_textwidth(card_string, 50)           
            canvas.draw_text(card_string, (text_pos, 75), 80, "White")
        else:
            canvas.draw_line((offset+25, 0), (offset+25, 100), 48, "Green")
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Restart", init, 100)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

# Always remember to review the grading rubric
