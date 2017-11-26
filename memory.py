# implementation of card game - Memory

import simplegui
import random

deck = [i + 1 for i in range(8) + range(8)]
previous_index1, previous_index2, score = 0, 0, 0

card_width = 50
card_height = 100
h_card_width = card_width / 2
h_card_height = card_height / 2

# helper function to initialize globals


def new_game():
    """Resets all the game parameters"""
    global deck, state, turned, state, score
    state, score = 0, 0
    label.set_text("Turns = %d" % score)
    random.shuffle(deck)
    turned = [False for i in deck]


# define event handlers
def mouseclick(pos):
    """Handles the click logic"""
    global turned, state, previous_index1, previous_index2, score
    card_click = pos[0] // card_width
    if not turned[card_click]:
        turned[card_click] = True
        if state == 0:
            state = 1
            previous_index1 = card_click
        elif state == 1:
            state = 2
            previous_index2 = previous_index1
            previous_index1 = card_click
        else:
            state = 1
            if deck[previous_index1] == deck[previous_index2]:
                turned[previous_index1] = True
                turned[previous_index2] = True
            else:
                turned[previous_index1] = False
                turned[previous_index2] = False
            score += 1
            label.set_text("Turns = %d" % score)
            previous_index2 = previous_index1
            previous_index1 = card_click

# cards are logically 50x100 pixels in size


def draw(canvas):
    """Draws numbers, and hiding cards"""
    for idx, card in enumerate(deck):
        canvas.draw_text(str(card), (idx * card_width +
                                     (h_card_width / 2), 70), 50, "Teal")
    for idx, card in enumerate(turned):
        if not turned[idx]:
            center = [idx * card_width + (h_card_width), h_card_height]
            canvas.draw_polygon([
                [center[0] - h_card_width, center[1] - h_card_height],
                [center[0] + h_card_width, center[1] - h_card_height],
                [center[0] + h_card_width, center[1] + h_card_height],
                [center[0] - h_card_width, center[1] + h_card_height]
            ], 2, 'Yellow', 'Orange')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = %d" % score)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
