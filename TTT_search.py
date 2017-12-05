"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    if board.check_win() is not None:
        return SCORES[board.check_win()], (-1, -1)
    else:
        possible_scores = []
        for cell in board.get_empty_squares():
            new_board = board.clone()
            new_board.move(cell[0], cell[1], player)
            if new_board.check_win() is not None:
                possible_scores.append((SCORES[new_board.check_win()], cell))
            else:
                if player == provided.PLAYERX:
                    opposite_player = provided.PLAYERO
                else:
                    opposite_player = provided.PLAYERX
                possible_scores.append((mm_move(new_board, opposite_player)[0], cell))
        if player == provided.PLAYERX:
            win_move = max(possible_scores)
        else:
            win_move = min(possible_scores)
        return win_move[0], win_move[1]
            
def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

#brd = [[provided.PLAYERO, provided.PLAYERO, provided.PLAYERX],
#       [provided.PLAYERX, provided.PLAYERX, provided.EMPTY],
#       [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]
#
#
#my_board = provided.TTTBoard(3, board = brd)
#print my_board
#print my_board.get_empty_squares()
#
#print mm_move(my_board, provided.PLAYERX)
