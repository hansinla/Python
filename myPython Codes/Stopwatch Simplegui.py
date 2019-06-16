# template for "Stopwatch: The Game"
import simplegui
# define global variables
BUTTON_WIDTH = 120
FRAME_SIZE_X = FRAME_SIZE_Y = 125
TIME_POS_X = 32
TIME_POS_Y= 70
SCORE_POS_X = 90
SCORE_POS_Y= 20
time = attempts = score = 0
stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    tenth_format = str(time % 10)
    seconds = (time // 10 ) % 60
    single_sec_format = str(seconds % 10)
    ten_sec_format = str (seconds // 10)
    min_format = str(time // 600)
    return min_format + ":" + ten_sec_format+single_sec_format + "." + tenth_format
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stopped
    timer.start()
    stopped = False

def stop():
    global stopped
    global attempts
    global score
    timer.stop()
    if (not stopped):
        attempts += 1
        if (time % 10 == 0):
            score += 1
    stopped = True

def reset():
    global time
    global attempts
    global score
    timer.stop()
    time = attempts = score = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time+=1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), (TIME_POS_X, TIME_POS_Y), 24, "Red")
    canvas.draw_text(str(score)+"/"+str(attempts), (SCORE_POS_X, SCORE_POS_Y), 18, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch", FRAME_SIZE_X, FRAME_SIZE_Y)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.add_button("START", start, BUTTON_WIDTH)
frame.add_button("STOP", stop, BUTTON_WIDTH)
frame.add_button("RESET", reset, BUTTON_WIDTH)
frame.set_draw_handler(draw_handler)

# start timer and frame
frame.start()

# Please remember to review the grading rubric
