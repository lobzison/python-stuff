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

# helper functions
import random

def name_to_number(name):
    """Converts name of entity into number"""
    if name == "rock":
        result = 0
    elif name == "Spock":
        result = 1
    elif name == "paper":
        result = 2
    elif name == "lizard":
        result = 3
    elif name == "scissors":
        result = 4
    else:
        return "Wrong entity given"
    return result


def number_to_name(number):
    """Converts number of entity into name"""
    if number == 0:
        result = "rock"
    elif number == 1:
        result = "Spock"
    elif number == 2:
        result = "paper"
    elif number == 3:
        result = "lizard"
    elif number == 4:
        result = "scissors"
    else:
        return "Wrong number given"
    return result
    

def rpsls(player_choice):
    """Reads players input, rolls programms choise,
    prints the winner"""
    #player
    print "\nPlayer chooses %s" % player_choice
    players_num = name_to_number(player_choice)
    #pc
    pc_num = random.randrange(0,5)
    print "Computer chooses %s" % number_to_name(pc_num)
    player_vs_pc = (players_num - pc_num) % 5
    #choose winner based on modulus
    if player_vs_pc == 0.0:
        print "Player and computer tie!"
    elif player_vs_pc >= 3.0:
        print "Computer wins!"
    else:
        print "Player wins!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

