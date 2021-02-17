# To run this game use this url: http://www.codeskulptor.org/#user48_avMvWYpaOr_8.py
# Mini-project #6 - Blackjack
# Created by GE

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
    
    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0] + 1, pos[1] + CARD_BACK_CENTER[1] + 1], CARD_BACK_SIZE)
    
# define hand class
class Hand:
    
    def __init__(self):
        self.hand = []

    def __str__(self):
        string = ''
        for c in self.hand:
            string += ' ' + str(c)
        return 'Hand contains: ' + string

    def add_card(self, card):
        self.card = card
        return self.hand.append(card)
    
    def get_value(self):
        self.value = 0
        for i in self.hand:
            self.value += VALUES[i.rank]
        for j in self.hand:
            if self.value + 10 <= 21 and VALUES[j.rank] == 1 :
                self.value += 10
        return self.value            
                    
    def draw(self, canvas, pos):
        for c in self.hand:
            pos[0] = pos[0] + CARD_SIZE[0] + 20
            c.draw(canvas, pos)

class Deck:
    def __init__(self):
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i, j))
       
    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def deal_card(self):
        return self.deck.pop(-1)

    def __str__(self):
        string = ''
        for c in self.deck:
            string += ' ' + str(c)
        return 'Deck contains:' + string 

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score
    if in_play:
        score -= 1
        in_play = False
        deal()
    else:
        deck = Deck()
        deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        outcome = 'Hit or Stand ?'
        in_play = True
    
def hit():
    global in_play, outcome, score

    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
            if player_hand.get_value() > 21:
                outcome = 'You are busted! Dealer wins. New deal ?'
                score -= 1
                in_play = False                    

def stand():
    global in_play, outcome, score
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        if (dealer_hand.get_value() <= 21) and (dealer_hand.get_value() >= player_hand.get_value()):
            outcome = 'Dealer wins! New deal ?'
            score -= 1
        elif dealer_hand.get_value() > 21:
            outcome = 'Dealer is busted! Player wins. New deal ?'
            score += 1
        else:
            outcome = ' Player wins! New deal ?'
            score += 1
    else: 
        outcome = ' Round was finished, press on "Deal"'
    in_play = False
    
# draw handler    
def draw(canvas):
    canvas.draw_text("BLACKJACK", (150, 70), 50, "Orange")
    canvas.draw_text('Dealer' , (36, 185), 30, "Black")
    canvas.draw_text('Player' , (36, 385), 30, "Black")
    canvas.draw_text(outcome, (50, 550), 30, "Orange")
    canvas.draw_text("Score: " + str(score), (245, 130), 30, "Black")
    player_hand.draw(canvas, [-65, 400])
    dealer_hand.draw(canvas, [-65, 200])
    if in_play:
        dealer_hand.hand[0].draw_back(canvas, [25, 199])

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
