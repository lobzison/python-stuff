"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""
import random

class SolitaireMancala_T:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = list(configuration)
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        temp = list(self._board)
        temp.reverse()
        return str(temp)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for idx in range(1, len(self._board)):
            if self._board[idx] != 0:
                return False
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        move_in_range = 0 < house_num < len(self._board)
        index_matches = self._board[house_num] == house_num
        return move_in_range and index_matches

    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):  
            for idx in range(house_num):
                self._board[idx] += 1
            self._board[house_num] = 0

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for house_num in range(1, len(self._board)):
            if self.is_legal_move(house_num):
                return house_num
        return 0
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        new_board = SolitaireMancala_T()
        new_board.set_board(self._board)
        move_list = []
        next_move =  new_board.choose_move()
        while next_move != 0:
            new_board.apply_move(next_move)
            move_list.append(next_move)
            next_move = new_board.choose_move()
        return move_list
    
class SolitaireMancala:

    def __init__(self):
        self._board = [0]

    def set_board(self, configuration):
        self._board = configuration[:]

    def __str__(self):
        return str([self._board[i] for i in range((len(self._board) - 1), (-1), (-1))])

    def get_num_seeds(self, house_num):
        return self._board[house_num]

    def is_legal_move(self, house_num):
        if ((house_num == 0) or (house_num >= len(self._board))):
            return False
        else:
            return (house_num == self._board[house_num])

    def apply_move(self, house_num):
        if self.is_legal_move(house_num):
            for i in range(house_num):
                self._board[i] += 1
            self._board[house_num] = 0

    def choose_move(self):
        for i in self._board[1:]:
            if self.is_legal_move(i):
                return i
        return 0

    def is_game_won(self):
        won = True
        for i in self._board[1:]:
            if (i != 0):
                won = False
        return won

    def plan_moves(self):
        moves = []
        while True:
            move = self.choose_move()
            if ((move == 0) or self.is_game_won()):
                break
            else:
                self.apply_move(move)
                moves.append(move)
        return moves
    
# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala_T()
    my_game2 = SolitaireMancala()
    config1 = [0, 0, 1, 1, 3, 5, 0, 2, 4, 0]    
    my_game.set_board(config1)   
    my_game2.set_board(config1) 
    print my_game.plan_moves()
    print my_game2.plan_moves()

def test():
    my_game = SolitaireMancala_T()
    my_game2 = SolitaireMancala()
    
    while True:
        config = [0]
        gen_config(config)
        my_game.set_board(config)
        my_game2.set_board(config)
        if my_game.plan_moves() != my_game2.plan_moves():
            print my_game.plan_moves()
            print my_game2.plan_moves()
            print config
            break

def gen_config(config):
    for ln in range(random.randrange(9)):
        config.append(random.randrange(10))
    return config
test()
#print(gen_config([0]))                  
                  