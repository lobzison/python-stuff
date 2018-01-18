"""
Computing global and loacl DNA alignments
"""

def build_scoring_matrix(alphabet, diag_score,
                         off_diag_score, dash_score):
    """
    Builds a scoring matrix in a form of dictionay of dictionaries
    returns the matrix
    """
    def get_score(inside_letter, outside_letter):
        """
        Get the correct score for pair
        """
        if outside_letter == "-" or inside_letter == "-":
            return dash_score
        elif outside_letter == inside_letter:
            return diag_score
        else:
            return off_diag_score
    extended_alphabet = "-" + alphabet
    outside_dict = {}
    for outside_letter in extended_alphabet:
        inside_dict = {inside_letter: get_score(inside_letter,
                                                outside_letter)
                       for inside_letter in extended_alphabet}
        outside_dict[outside_letter] = inside_dict
    return outside_dict

# test = build_scoring_matrix("abcd", 10, 1, -1)

# print test