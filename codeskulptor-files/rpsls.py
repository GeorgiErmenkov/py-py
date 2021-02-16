# To run the game use this url : http://www.codeskulptor.org/#user48_urTaMlIwBN_1.py
#
# Rock-paper-scissors-lizard-Spock template
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random


def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 'Error:name not existent in the game.'


def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'Error:name not existent in the game.'
    

def rpsls(player_choice): 
    print ''
    print 'The player has chosen: ' + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print 'The computer has chosen: ' + comp_choice
    difference = (player_number - comp_number) % 5
    if (difference == 1) or ( difference == 2):
        print 'Player wins'
    elif (difference == 3) or (difference == 4):
        print 'Computer wins'
    else:
        print 'Its a tie'
    

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
