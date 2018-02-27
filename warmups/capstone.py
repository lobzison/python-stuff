def test1():
    """returns nuothing"""
    return

print(test1())

my_dict = {(0): 1}

print(my_dict)

class BankAccount:
    def __init__(self, initial_balance):
        """
        Creates an account with the given balance.
        """
        self.balance = initial_balance
        self.fees = 0
        self.fee = 5

    def deposit(self, amount):
        """
        Deposits the amount into the account.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  
        Each withdrawal resulting in a balance of 
        less than 10 dollars (before any fees) also 
        deducts a penalty fee of 5 dollars from the balance.
        """
        if self.balance - amount < 10:
            self.fees += self.fee
            self.balance -= self.fee
        self.balance -= amount

    def get_balance(self):
        """
        Returns the current balance in the account.
        """
        return self.balance

    def get_fees(self):
        """
        Returns the total fees ever deducted from the account.
        """
        return self.fees

account1 = BankAccount(20)
account1.deposit(10)
account2 = BankAccount(10)
account2.deposit(10)
account2.withdraw(50)
account1.withdraw(15)
account1.withdraw(10)
account2.deposit(30)
account2.withdraw(15)
account1.deposit(5)
account1.withdraw(20)
account2.withdraw(15)
account2.deposit(25)
account2.withdraw(15)
account1.deposit(10)
account1.withdraw(50)
account2.deposit(25)
account2.deposit(25)
account1.deposit(30)
account2.deposit(10)
account1.withdraw(15)
account2.withdraw(10)
account1.withdraw(10)
account2.deposit(15)
account2.deposit(10)
account2.withdraw(15)
account1.deposit(15)
account1.withdraw(20)
account2.withdraw(10)
account2.deposit(5)
account2.withdraw(10)
account1.deposit(10)
account1.deposit(20)
account2.withdraw(10)
account2.deposit(5)
account1.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account2.deposit(10)
account2.deposit(15)
account2.deposit(20)
account1.withdraw(15)
account2.deposit(10)
account1.deposit(25)
account1.deposit(15)
account1.deposit(10)
account1.withdraw(10)
account1.deposit(10)
account2.deposit(20)
account2.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account1.deposit(10)
account2.withdraw(20)
print (account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees())


# Rock-paper-scissors-lizard-Spock template

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"        
    else:
        return "scissors"
    
def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    else:
        return 4

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print()
    
    # print( out the message for the player's choice)
    print( "Player chooses", player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print( out message for computer's choice)
    print( "Computer chooses", comp_choice)

    # compute difference of player_number and comp_number modulo five
    difference = comp_number - player_number % 5
    # assert difference == (comp_number - player_number) % 5
    print(difference)
    print((comp_number - player_number) % 5)

    # use if/elif/else to determine winner and print( winner message)
    if difference == 0:
        print( "Player and computer tie!")
    elif (difference == 1) or (difference == 2):
        print( "Computer wins!")
    else:
        print( "Player wins!")
        
    

     
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


crazy = [1, 1]
crazy = crazy[1]
print(crazy)


print((1/6) ** 5)

def probability(outcomes):
    """
    Computes probabiliti of outcomes sequence
    with hardcoded chanches
    The die has a 0.1 probability of landing on 1, a 0.2 probability of landing on 2,
     a 0.3 probability of landing on 3, a 0.15 probability of landing on 4,
      a 0.05 probability of landing on 5, and a 0.2 probability of landing on 6.
    """
    chances = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.15, 5: 0.05, 6: 0.2}
    result = 1
    for outcome in outcomes:
        result *= chances[outcome]
    return result

print(probability([4, 2, 6, 4, 2, 4, 5, 5, 5, 5, 1, 2, 6, 2, 6, 6, 4, 6, 2, 3, 5, 5, 2,
                   1, 5, 5, 3, 2, 1, 4, 4, 1, 6, 6, 4, 6, 2, 4, 3, 2, 5, 1, 3, 5, 4, 1, 2, 3, 6, 1]))

# question 14 ?????

# 15 n * (n - 1) * ... * 1

# 10 17 13 20


# 10, 13, 20, 17, 4, 7, 12, 19, 23, 5, 1, 0, 2

# 20, 13, 10, 17, 19, 7, 12, 4, 23, 1, 5, 2, 0

print('-'*30)
def pick_a_number(board, player):
    """
    takes a list representing the game board and returns 
    a tuple that is the score of the game if both players
    play optimally. Here, optimal play means that the player
    maximizes his/her final score. The returned tuple should
    be ordered with the current player's score first and the
    other player's score second.
    """
    if len(board) == 0:
        return (0, 0)
    if len(board) == 1:
        if player == 0:
            return (board[0], 0)
        else:
            return(0, board[0])
    print(board, player)
    scores1 = pick_a_number(board[1:],  (player + 1) %2)
    if player == 0:
        upd_scores1 = (scores1[0] + board[0], scores1[1])
    else:
        upd_scores1 = (scores1[0], scores1[1] + board[0])

    scores2 = pick_a_number(board[:-1], (player + 1) %2)
    if player == 0:
        upd_scores2 = (scores2[0] + board[-1], scores2[1])
    else:
        upd_scores2 = (scores2[0], scores2[1] + board[-1])
    
    score = max(upd_scores1, upd_scores2 ,key=lambda x:x[player])
    return score
    
# print(pick_a_number([12, 9, 7, 3, 4, 7, 4, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1], 0))

#print(pick_a_number([12, 9, 7, 3, 4, 7, 4, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1], 0))
# 69 67
# print([3, 5, 2, 1][:-1], [3, 5, 2, 1][1:])

"""
Example graphs for Question 25 on the Capstone Exam
"""

# Example graphs

GRAPH1 = {1 : set([]), 2 : set([3, 7]), 3 : set([2, 4]), 4 : set([3, 5]), 5 : set([4, 6]), 6 : set([5, 7]), 7 : set([2, 6])}

GRAPH2 = {1 : set([2, 3, 4, 5, 6, 7]), 2 : set([1]), 3 : set([1]), 4 : set([1]), 5 : set([1]), 6 : set([1]), 7 : set([1])}

GRAPH3 = {0: set([4, 7, 10]), 1: set([5, 6]), 2: set([7, 11]), 3: set([10]), 4: set([0, 7, 11]), 5: set([1, 7]), 6: set([1]), 7: set([0, 2, 4, 5, 9, 11]), 8: set([9]), 9: set([7, 8]), 10: set([0, 3]), 11: set([2, 4, 7])}

GRAPH4 = {0: set([4, 7, 10, 12, 13]), 1: set([5, 6, 12]), 2: set([7, 11, 12, 14]), 3: set([10, 14, 15]), 4: set([0, 7, 11, 12, 13, 14]), 5: set([1, 7, 15]), 6: set([1, 13]), 7: set([0, 2, 4, 5, 9, 11, 14]), 8: set([9, 14, 15]), 9: set([7, 8]), 10: set([0, 3]), 11: set([2, 4, 7]), 12: set([0, 1, 2, 4]), 13: set([0, 4, 6, 15]), 14: set([2, 3, 4, 7, 8]), 15: set([3, 5, 8, 13])}

GRAPH5 = {0: set([4, 7, 10, 12, 13, 16]), 1: set([5, 6, 12]), 2: set([7, 11, 12, 14]), 3: set([10, 14, 15]), 4: set([0, 7, 11, 12, 13, 14, 17]), 5: set([1, 7, 15]), 6: set([1, 13]), 7: set([0, 2, 4, 5, 9, 11, 14, 18]), 8: set([9, 14, 15]), 9: set([7, 8, 19]), 10: set([0, 3]), 11: set([2, 4, 7]), 12: set([0, 1, 2, 4]), 13: set([0, 4, 6, 15, 16]), 14: set([2, 3, 4, 7, 8]), 15: set([3, 5, 8, 13]), 16: set([0, 13, 19]), 17: set([4]), 18: set([7]), 19: set([9, 16])}

GRAPH6 = {0: set([4, 7, 10, 12, 13, 16]), 1: set([5, 6, 12]), 2: set([7, 11, 12, 14]), 3: set([10, 14, 15]), 4: set([0, 7, 11, 12, 13, 14, 17]), 5: set([1, 7, 15]), 6: set([1, 13]), 7: set([0, 2, 4, 5, 9, 11, 14, 18]), 8: set([9, 14, 15]), 9: set([7, 8, 19]), 10: set([0, 3]), 11: set([2, 4, 7]), 12: set([0, 1, 2, 4]), 13: set([0, 4, 6, 15, 16]), 14: set([2, 3, 4, 7, 8]), 15: set([3, 5, 8, 13]), 16: set([0, 13, 17, 19]), 17: set([4, 16]), 18: set([7]), 19: set([9, 16])}

def mystery(graph):
    """
    Takes graph as an input in form of ajacency list adn returns
    A subset V′⊆V of minimum size such that every edge in E has at least one of its endpoints in V′
    """
    return graph

# Testing 
print(len(mystery(GRAPH1)))     # answer should be 3
print(len(mystery(GRAPH2)))     # answer should be 1
print(len(mystery(GRAPH3)))     # answer should be 6
print(len(mystery(GRAPH4)))     # answer should be 9
print(len(mystery(GRAPH5)))
print(len(mystery(GRAPH6)))

