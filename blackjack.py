# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
winner = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

    def draw_fold(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], 
                    CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        res = 'Hand contains:'
        for card in self.hand:
            res += card.get_suit() + card.get_rank() + ' '
        return res

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        result = 0
        aces = any(card.get_rank() == 'A' for card in self.hand)
        
        for card in self.hand:
            result += VALUES[card.get_rank()]
        if aces and result + 10 <= 21:
            result += 10
        return result
   
    def draw(self, canvas, pos, dealer = 0):
        i = 0
        space = 20
        for card in self.hand:
            card.draw(canvas,[pos[0] + CARD_SIZE[0] * i + 20, pos[1]])
            if dealer == 1 and i == 0:
                card.draw_fold(canvas,[pos[0] + CARD_SIZE[0] * i + 20, pos[1]])
            i += 1
        
 

class Deck:
    def __init__(self):
        self.deck = [Card(s, r) for s in SUITS for r in RANKS]
        
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        res = "Deck contains: "
        for card in self.deck:
            res += str(card) + ' '
        return res

#define event handlers for buttons
def deal():
    global outcome, in_play, play_deck, p_hand, d_hand, score, winner

    play_deck = Deck()
    play_deck.shuffle()
    p_hand = Hand()
    d_hand = Hand()
    
    p_hand.add_card(play_deck.deal_card())
    p_hand.add_card(play_deck.deal_card())
    
    d_hand.add_card(play_deck.deal_card())
    d_hand.add_card(play_deck.deal_card())
    
    outcome = "Hit or Stand?"
    winner = ""
    
    if in_play:
        score -= 1
        winner = "Dealer won!"
        

    in_play = True

def hit():
    global p_hand, outcome, in_play, score, winner
    if in_play:
        
        if p_hand.get_value() > 21:
            outcome = "Deal a new one?"
            in_play = False
            score -= 1
            winner = "Dealer won!"
        else:
            p_hand.add_card(play_deck.deal_card())
            outcome = "Hit or Stand?"
       
def stand():
    global outcome, in_play, score, winner
    if in_play:
        outcome = "Deal a new one?"
        in_play = False
        if p_hand.get_value() > 21:
            score -= 1
            winner = "Dealer won!"
        else:
            while d_hand.get_value() < 17:
                d_hand.add_card(play_deck.deal_card())
            if d_hand.get_value() > 21:
                score += 1
                winner = "Player won!"
            else:
                if d_hand.get_value() >= p_hand.get_value():
                    score -= 1
                    winner = "Dealer won!"
                else:
                    score += 1
                    winner = "Player won!"
            

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    p_hand.draw(canvas, [100,400])
    if in_play:
        d_hand.draw(canvas, [100,200], 1)
    else:
        d_hand.draw(canvas, [100,200])

    canvas.draw_text(outcome, [300, 380], 30, "Black")
    canvas.draw_text(str(score), [500, 100], 40, "Black")
    canvas.draw_text(winner, [300, 350], 40, "Black")
    
    canvas.draw_text("Player", [120, 380], 40, "Black")
    canvas.draw_text("Dealer", [120, 180], 40, "Black")
    canvas.draw_text("BlackJack", [100, 100], 60, "Black")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)



# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
