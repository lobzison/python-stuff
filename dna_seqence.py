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


def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    Builds a scoring matrix in a form of dictionay of dictionaries
    returns the matrix
    """
    extended_alphabet = "-" + alphabet
    outside_dict = {}
    for outside_letter in extended_alphabet:
        inside_dict = {}
        for inside_letter in extended_alphabet:
            if outside_letter == "-" or inside_letter == "-":
                inside_dict[inside_letter] = dash_score
            elif outside_letter == inside_letter:
                inside_dict[inside_letter] = diag_score
            else:
                inside_dict[inside_letter] = off_diag_score
        outside_dict[outside_letter] = inside_dict
    return outside_dict

a = build_scoring_matrix("abcd", 10, 1, -1)

print a
