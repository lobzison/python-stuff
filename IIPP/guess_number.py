import simplegui
import random
import math

# helper function to start and restart the game


def new_game(range=100):
    global pc_num, guesses_left
    pc_num = random.randrange(1, range)
    print "New game. Range is from 1 to %d" % range
    if range == 1000:
        guesses_left = 10
    else:
        guesses_left = 7
    print "Number of remaining guesses is %d\n" % guesses_left

# define event handlers for control panel


def range100():
    new_game(100)


def range1000():
    new_game(1000)


def input_guess(guess):
    global pc_num, guesses_left
    guess_num = int(float(guess))
    print "Guess was %d" % guess_num
    guesses_left -= 1
    print "Number of remaining guesses is %d" % guesses_left
    if pc_num == guess_num:
        print "Correct!\n"
        new_game()
    elif pc_num > guess_num:
        print "Higher!\n"
    elif pc_num < guess_num:
        print "Lower!\n"
    if guesses_left <= 0:
        new_game()


# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame
frame.add_button("Range is [0:100)", range100, 200)
frame.add_button("Range is [0:1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)


# call new_game
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
