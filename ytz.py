"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def gen_all_perms(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                if item not in new_sequence:
                    new_sequence.append(item)
                    temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def gen_sorted_perms(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """
    all_perms = gen_all_perms(outcomes, length)
    sorted_perms = [tuple(sorted(perm)) for perm in all_perms]
    return set(sorted_perms)


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    scores = []
    scr = 0
    for s_index, value in enumerate(hand):
        if s_index == 0:
            scr += value
        else:
            if value != hand[s_index - 1]:
                scores.append(scr)
                scr = value
            else:
                scr += value
    scores.append(scr)

    return max(scores)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = list(range(1, num_die_sides + 1))
    possible_sides = gen_all_sequences(outcomes, num_free_dice)
    overall_score = 0
    for combo in possible_sides:
        held, roll = list(held_dice), list(combo)
        hand = held + roll
        hand_score = score(tuple(sorted(hand)))
        overall_score += hand_score

    return float(overall_score) / len(possible_sides)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    result = set([()])
    length = len(hand)
    for index in range(length):
        perms = gen_sorted_perms(tuple(range(length)), index + 1)
        perms = set([tuple([hand[index] for index in tpl]) for tpl in perms])
        result.update(perms)
    return result


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    holds = gen_all_holds(hand)
    hand_size = len(hand)
    expected_values = [(expected_value(hold, num_die_sides,
                                       hand_size - len(hold)), hold)
                       for hold in holds]
    best_str = max(expected_values)
    return best_str


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score


run_example()


# import poc_holds_testsuite
# poc_holds_testsuite.run_suite(gen_all_holds)
