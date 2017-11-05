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
LEFT = False
RIGHT = True
ball_vel = [0,0]
ball_pos = []
mult = 2

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, ball_speed # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    x = random.randrange(2, 4)
    y = random.randrange(1, 3) 
    if direction == "RIGHT":
        ball_vel = [x, -y]
    if direction == "LEFT":
        ball_vel = [-x, -y]    
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, acc  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball("RIGHT")
    paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    paddle1_vel = 0
    paddle2_vel = 0
    acc = 1.1
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1), (150, 50), 46, 'Gray', 'monospace')
    canvas.draw_text(str(score2), (450, 50), 46, 'Gray', 'monospace')
    # update ball
    ball_pos[0] += ball_vel[0] * mult
    ball_pos[1] += ball_vel[1] * mult
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 4, "Teal", "Teal")
    # balls collision with horisontal edges
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * acc
            ball_vel[1] =  ball_vel[1] * acc
        else:
            score2 += 1
            spawn_ball("RIGHT")
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * acc
            ball_vel[1] =  ball_vel[1] * acc
        else:
            score1 += 1
            spawn_ball("LEFT")  
        
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    
    if paddle1_pos + paddle1_vel> 0 and paddle1_pos + PAD_HEIGHT + paddle1_vel < HEIGHT:
        paddle1_pos += paddle1_vel
        
    if paddle2_pos + paddle2_vel> 0 and paddle2_pos + PAD_HEIGHT + paddle2_vel < HEIGHT:
        paddle2_pos += paddle2_vel
    
    canvas.draw_polygon([[0, paddle1_pos],
                        [PAD_WIDTH, paddle1_pos], 
                        [PAD_WIDTH, paddle1_pos + PAD_HEIGHT],
                        [0, paddle1_pos + PAD_HEIGHT]],
                        1, 'Orange', 'Orange')
    
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos],
                        [WIDTH, paddle2_pos], 
                        [WIDTH, paddle2_pos + PAD_HEIGHT],
                        [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT]],
                        1, 'Orange', 'Orange')
    
    # determine whether paddle and ball collide    

    # draw scores
    
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -10
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 10
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -10
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 10
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Restart', new_game)

# start frame
new_game()
frame.start()
