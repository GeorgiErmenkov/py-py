# To run the game use this url: https://py2.codeskulptor.org/#user48_ztU9Xp0B40_4.py

"""
Monte Carlo Tic-Tac-Toe Player
"""
# Assignment: Tic-Tac-Toe (Monte Carlo)
# Created by: GE

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.

NTRIALS = 30         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

def mc_trial(board, player):
    '''
    This function takes a current board and the next player to move. 
    The function should play a game starting with the given player by 
    making random moves, alternating between players. The function should 
    return when the game is over. 
    '''
    while board.check_win() == None:
        empty_squares_list = board.get_empty_squares()
        ran_choice = random.choice(empty_squares_list)
        board.move(ran_choice[0], ran_choice[1], player)
        player = provided.switch_player(player)

        
def mc_update_scores(scores, board, player):
    '''
    This function takes a grid of scores (a list of lists) with the same 
    dimensions as the Tic-Tac-Toe board, a board from a completed game, and 
    which player the machine player is. The function should score the 
    completed board and update the scores grid. 
    '''
    for dummy_row in range(board.get_dim()):
        for dummy_pos in range(board.get_dim()):
            if player == board.check_win():
                if board.square(dummy_row, dummy_pos) == player:
                    scores[dummy_row][dummy_pos] += SCORE_CURRENT
                elif board.square(dummy_row, dummy_pos) == provided.switch_player(player):
                    scores[dummy_row][dummy_pos] -= SCORE_OTHER
            elif provided.switch_player(player) == board.check_win():
                if board.square(dummy_row, dummy_pos) == player:
                    scores[dummy_row][dummy_pos] -= SCORE_CURRENT
                elif board.square(dummy_row, dummy_pos) == provided.switch_player(player):
                    scores[dummy_row][dummy_pos] += SCORE_OTHER

        
def get_best_move(board,scores):
    '''
    This function takes a current board and a grid of scores. The function 
    should find all of the empty squares with the maximum score and randomly 
    return one of them as a tuple. 
    '''
    best_moves_list = []
    empty_score_list = []
    best_score = None
    for square_tuple in board.get_empty_squares():
        empty_score_list.append(scores[square_tuple[0]][square_tuple[1]])
    best_score = max(empty_score_list)
    
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if scores[row][col] == best_score:
                if board.square(row, col) == provided.EMPTY:
                    best_moves_list.append((row, col))
    
    return random.choice(best_moves_list)
    

def mc_move(board, player, trials):
    '''
     This function takes a current board, which player the machine 
     player is, and the number of trials to run. The function should use 
     the Monte Carlo simulation described above to return a move for the 
     machine player in the form of a (row, column) tuple.
    '''
    scores = [[0 for dummy_row in range(board.get_dim())] for dummy_col in range(board.get_dim())] 

    for dummy_trial in range(trials):
        trial_board = board.clone()
        mc_trial(trial_board, player)
        mc_update_scores(scores, trial_board, player)
    
    return get_best_move(board, scores)



# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
