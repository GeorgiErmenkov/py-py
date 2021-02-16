# To run the game use this url : http://www.codeskulptor.org/#user48_Ul4V5IJtlv_1.py
#
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random


# initialize global variables used in your code here
num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0, num_range)
    global num_guess
    if num_range == 100:
        num_guess = 7
    elif num_range == 1000:
        num_guess = 10
    frame.start()
    print 'New game. Range is from 0 to', num_range
    print 'Number of remaining guesses is', num_guess
    print ''
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
   

def input_guess(guess):
    # main game logic goes here	
    global num_guess
    num_guess -= 1
    num = int(guess)
    print 'Guess was:', num
    if num_guess >= 0:
        if secret_number < num:
            print 'Lower'
        elif secret_number > num:
            print 'Higher'
        else:
            print 'Correct!'
            print ''
            return new_game()
    else:
        print 'Out of guesses. Try again.'
        print ''
        return new_game()
    print 'Number of remaining guesses is:', num_guess
    print ''
        
# create frame
frame = simplegui.create_frame('Guess the number', 150, 250)

# register event handlers for control elements and start frame
inp = frame.add_input('Enter your guess(a number):', input_guess, 180)
button100 = frame.add_button("Range is [0,100)", range100)
button1000 = frame.add_button('Range is [0,1000)', range1000)

# call new_game 
new_game()
