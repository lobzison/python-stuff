"""
Implementation of recursive and DP algorithms
for RNA secondary structure problem
"""


def is_legit(first_letter, second_letter):
    """
    Check if two structures can be folded
    """
    l_one = min(first_letter, second_letter)
    l_two = max(first_letter, second_letter)
    if (l_one == "A" and l_two == "U" or
            l_one == "C" and l_two == "G"):
        return True
    else:
        return False


def recursive_implementation(rna_sequence):
    """
    Recursive implementation of rna sequence problem
    returns the max number of folds
    """
    if len(rna_sequence) <= 4:
        return 0
    # res = max(recursive_implementation(rna_sequence[:-1]), )




print a
