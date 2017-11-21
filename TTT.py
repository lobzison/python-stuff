"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 1 # Score for squares played by the current player
SCORE_OTHER = 1  # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
    """
    Mutates a board to have a finished random game
    """
    players = {1: provided.PLAYERX, 2: provided.PLAYERO}
    p_index = players.keys()[players.values().index(player)]
    
    cells = board.get_empty_squares()
    random.shuffle(cells)
    for cell in cells:
            board.move(cell[0], cell[1], players[p_index])
            p_index = (p_index % 2) + 1
            if board.check_win() != None:
                break
    
def mc_update_scores(scores, board, player):
    """
    Mutates scores calculated from the board
    """
    p_scores = SCORE_CURRENT
    o_scores = SCORE_OTHER
    if board.check_win() == player:
        o_scores *= -1
    elif board.check_win() == provided.DRAW:
        p_scores = 0
        o_scores = 0
    else:
        p_scores *= -1
        
    for r_idx, row in enumerate(scores):
        for c_idx, _ in enumerate(row):
            value = board.square(r_idx, c_idx)
            if value == player:
                scores[r_idx][c_idx] += p_scores
            elif value == provided.EMPTY:
                scores[r_idx][c_idx] += 0
            else:
                scores[r_idx][c_idx] += o_scores
    

def get_best_move(board, scores):
    """
    Returns the best move based on score
    """
    empty_cells = board.get_empty_squares()
    _, max_index = max((cell, (r_index, c_index))
                               for r_index, row in enumerate(scores)
                               for c_index, cell in enumerate(row)
                               if (r_index, c_index) in empty_cells)
    return max_index
    

def mc_move(board, player, trials):
    """
    Returns the best move for player
    """
    scores = mc_make_scores_grid(board)
    for _ in range(trials):
        clone = board.clone()
        mc_trial(clone, player)
        mc_update_scores(scores, clone, player)
    
    cell = get_best_move(board, scores)
    return cell

def mc_make_scores_grid(board):
    """
    Makes a grid of scores
    """
    dim = board.get_dim()
    grid = [[0 for _ in range(dim)] for _ in range(dim)]
    return grid

#board = provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY],
#                                     [provided.PLAYERO, provided.PLAYERO, provided.EMPTY],
#                                     [provided.EMPTY, provided.PLAYERX, provided.EMPTY]])
#print board
#for i in range(1):
#    print mc_move(board, provided.PLAYERX, NTRIALS)




# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, mc_move, NTRIALS, False)
