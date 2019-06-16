# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
SCORE_SIZE = 35
ACC = 8
BALL_ACC = 1.1

# helper function that spawns a ball
def ball_init(right):
    global ball_pos, ball_vel 				# these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]			# set ball in middle of frame
    ball_vel = [random.randrange(2,4),-random.randrange(1,3)] #randomize ball velocity  
    if (not right):							# if right is True, the ball's velocity is upper right,
        ball_vel[0] = -ball_vel[0]			# else upper left
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel	# these are floats
    global score1, score2										# these are ints 
    score1 = score2 = 0											# initialize scores
    paddle1_vel = paddle2_vel = 0								# initialize paddle velocities
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]	# initialize paddle positions
    paddle2_pos = [WIDTH-HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]
    
    ball_init(random.choice([True, False]))						# call ball_init with random vector
    
def draw(c):
    global score1, score2, ball_pos, ball_vel
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
 
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos[1] >= 0 and paddle1_vel < 0) or (paddle1_pos[1] <= HEIGHT - PAD_HEIGHT and paddle1_vel > 0):
        paddle1_pos[1] = paddle1_pos[1] + paddle1_vel
    if (paddle2_pos[1] >= 0 and paddle2_vel < 0) or (paddle2_pos[1] <= HEIGHT - PAD_HEIGHT and paddle2_vel > 0):
        paddle2_pos[1] = paddle2_pos[1] + paddle2_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line(paddle1_pos, [paddle1_pos[0], paddle1_pos[1]+PAD_HEIGHT] , PAD_WIDTH, "White")
    c.draw_line(paddle2_pos, [paddle2_pos[0], paddle2_pos[1]+PAD_HEIGHT] , PAD_WIDTH, "White")
     
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # check for collision with top or bottom
    if (ball_pos[1] >= HEIGHT-1-BALL_RADIUS) or (ball_pos[1] <= BALL_RADIUS):
        ball_vel[1]= -ball_vel[1]
        
    # check for collision with right gutter
    if (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS):	# check for collision with right paddle
        if (ball_pos[1] > paddle2_pos[1] and ball_pos[1] < paddle2_pos[1] + PAD_HEIGHT):
            ball_vel[0] = -BALL_ACC * ball_vel[0]			# on collsion, bounce ball and increase speed
            ball_vel[1] = BALL_ACC * ball_vel[1]
        else:
            score1 += 1										# else ball hit gutter, increase score
            ball_init(False)								# spawn new ball with correct initial direction
               
    # check for collision with left gutter
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS):			# check for collision with left paddle
        if (ball_pos[1] > paddle1_pos[1] and ball_pos[1] < paddle1_pos[1] + PAD_HEIGHT):
            ball_vel[0] = -BALL_ACC * ball_vel[0]			# on collsion, bounce ball and increase speed
            ball_vel[1] = BALL_ACC * ball_vel[1]
        else:
            score2 += 1										# else ball hit gutter, increase score
            ball_init(True)									# spawn new ball with correct initial direction
            
    # calculate the size of the scores and where to draw them, and then do so
    text_pos_score1 =  WIDTH/4 - 0.5 * frame.get_canvas_textwidth(str(score1), SCORE_SIZE, "monospace")
    text_pos_score2 =  WIDTH*3/4 - 0.5 * frame.get_canvas_textwidth(str(score2), SCORE_SIZE, "monospace")  
    c.draw_text(str(score1), (text_pos_score1, SCORE_SIZE), SCORE_SIZE, "White", "monospace")
    c.draw_text(str(score2), (text_pos_score2, SCORE_SIZE), SCORE_SIZE, "White", "monospace")
            
def keydown(key):	# keydown handler to increase paddle velocity
    global paddle1_vel, paddle2_vel, ACC   
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= ACC
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += ACC
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += ACC
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= ACC
   
def keyup(key):		# keydown handler to decrease paddle velocity
    global paddle1_vel, paddle2_vel, ACC   
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel += ACC
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel -= ACC
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel -= ACC
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel += ACC

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("Restart", new_game, 150)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
new_game()
