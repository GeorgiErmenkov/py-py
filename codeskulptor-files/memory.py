# To run this game use this ulr : http://www.codeskulptor.org/#user48_CQdZijda1P_4.py
#
# implementation of card game - Memory
# Created by Georgi Ermenkov

import simplegui
import random

NUM_C = 16
CARD_WIDTH = 50
CARD_HEIGHT = 100
WIDTH = CARD_WIDTH * NUM_C
HEIGHT = CARD_HEIGHT

# helper function to initialize globals
def new_game():
    
    global deck1, deck2, game_deck, state, exposed, num_turns, card1, card2
    game_deck = [n for n in range(0, 8)] * 2
    random.shuffle(game_deck) 
    num_turns, state = 0, 0
    card1 = 0
    card2 = 0
    exposed = [False for n in range(0,16)]
    label.set_text("Turns = " + str(num_turns))
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, num_turns, card1, card2
    card_index = pos[0] // CARD_WIDTH
    if exposed[card_index] == False:
        if state == 0:
            exposed[card_index] = True
            card1 = card_index
            state = 1
        elif state == 1:
            exposed[card_index] = True
            card2 = card_index
            state = 2
            num_turns += 1
            label.set_text("Turns = " + str(num_turns))
        else:
            if game_deck[card1] != game_deck[card2]:
                exposed[card1] = exposed[card2] = False
            card1 = card_index
            exposed[card_index] = True
            state = 1            
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    for i in range(0,16):
        if exposed[i] == True:
            canvas.draw_polygon([[i * CARD_WIDTH, 0], [(i+1) * CARD_WIDTH, 0],
                                [(i + 1) * CARD_WIDTH, HEIGHT], [i * CARD_WIDTH, HEIGHT]], 1,
                                "Black", "White")
            canvas.draw_text(str(game_deck[i]), [i * CARD_WIDTH, CARD_HEIGHT - 20], CARD_HEIGHT, 'Black')
        else:
            canvas.draw_polygon([[i * CARD_WIDTH, 0], [(i+1) * CARD_WIDTH, 0],
                                [(i + 1) * CARD_WIDTH, HEIGHT], [i * CARD_WIDTH, HEIGHT]], 1,
                                "Black", "Green")           

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.set_canvas_background('White')
frame.add_button("Reset", new_game)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
label = frame.add_label("Turns = 0")
    
# get things rolling
new_game()
frame.start()
