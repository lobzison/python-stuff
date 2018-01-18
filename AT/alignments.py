
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
    extended_alphabet = alphabet.copy()
    extended_alphabet.add("-")
    outside_dict = {}
    for outside_letter in extended_alphabet:
        inside_dict = {inside_letter: get_score(inside_letter,
                                                outside_letter)
                       for inside_letter in extended_alphabet}
        outside_dict[outside_letter] = inside_dict
    return outside_dict

#test_ =  build_scoring_matrix(set(['A', 'C', 'T', 'G']), 10, 4, -6)
#print(test_)

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    Takes two sequences and scoring matrix for the same sybols
    Returns scored matrix
    """
    len_x = len(seq_x)
    len_y = len(seq_y)
    a_matrix = []
    for _ in range(len_x + 1):
        a_matrix.append([0 for _ in range(len_y + 1)])
    a_matrix[0][0] = 0
    for x_ind in range(1, len_x + 1):
        val = a_matrix[x_ind - 1][0] + scoring_matrix["-"][seq_x[x_ind - 1]]
        if global_flag or val > 0:
            a_matrix[x_ind][0] = val
    for y_ind in range(1, len_y + 1):
        val = a_matrix[0][y_ind - 1] + scoring_matrix["-"][seq_y[y_ind - 1]]
        if global_flag or val > 0:
            a_matrix[0][y_ind] = val
    for x_ind in range(1, len_x + 1):
        for y_ind in range(1, len_y + 1):
            val1 = a_matrix[x_ind - 1][y_ind - 1] + scoring_matrix[seq_y[y_ind - 1]][seq_x[x_ind - 1]]
            val2 = a_matrix[x_ind - 1][y_ind] + scoring_matrix[seq_x[x_ind - 1]]["-"]
            val3 = val = a_matrix[x_ind][y_ind - 1] + scoring_matrix["-"][seq_y[y_ind - 1]]
            val = max(val1, val2, val3)
            if global_flag or val > 0:
                a_matrix[x_ind][y_ind] = val
    return a_matrix

#test2_ = compute_alignment_matrix('AA', 'TAAT', test_, False)
#for line in test2_:
#    print(line)

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Computes global alingment
    Returns tuple with alignment score, anb both alignment
    """
    x_ind, y_ind = len(seq_x), len(seq_y)
    x_alig, y_alig = "", ""
    score = alignment_matrix[x_ind][y_ind]
    while x_ind != 0 and y_ind != 0:
        if alignment_matrix[x_ind][y_ind] == alignment_matrix[x_ind - 1][y_ind - 1] + scoring_matrix[seq_x[x_ind - 1]][seq_y[y_ind - 1]]:
            x_alig = seq_x[x_ind - 1] + x_alig
            y_alig = seq_y[y_ind - 1] + y_alig
            x_ind -= 1
            y_ind -= 1
        elif alignment_matrix[x_ind][y_ind] == alignment_matrix[x_ind - 1][y_ind] + scoring_matrix[seq_x[x_ind - 1]]["-"]:
            x_alig = seq_x[x_ind - 1] + x_alig
            y_alig = "-" + y_alig
            x_ind -= 1
        else:
            y_alig = seq_y[y_ind - 1] + y_alig
            x_alig = "-" + x_alig
            y_ind -= 1
    while x_ind != 0:
        x_alig = seq_x[x_ind - 1] + x_alig
        y_alig = "-" + y_alig
        x_ind -= 1
    while y_ind != 0:
        y_alig = seq_y[y_ind - 1] + y_alig
        x_alig = "-" + x_alig
        y_ind -= 1
    return (score, x_alig, y_alig)
#        
#print(compute_global_alignment('AA', 'TAAT',test_, test2_))

def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Computes local alingment
    Returns tuple with alignment score, anb both alignment
    """
    score, x_ind, y_ind = max(((scr, x, y)
                               for x, row in enumerate(alignment_matrix)
                               for y, scr in enumerate(row)))
    x_alig, y_alig = "", ""
    while x_ind != 0 and y_ind != 0:
        if alignment_matrix[x_ind][y_ind] == alignment_matrix[x_ind - 1][y_ind - 1] + scoring_matrix[seq_x[x_ind - 1]][seq_y[y_ind - 1]]:
            x_alig = seq_x[x_ind - 1] + x_alig
            y_alig = seq_y[y_ind - 1] + y_alig
            x_ind -= 1
            y_ind -= 1
        elif alignment_matrix[x_ind][y_ind] == alignment_matrix[x_ind - 1][y_ind] + scoring_matrix[seq_x[x_ind - 1]]["-"]:
            x_alig = seq_x[x_ind - 1] + x_alig
            y_alig = "-" + y_alig
            x_ind -= 1
        else:
            y_alig = seq_y[y_ind - 1] + y_alig
            x_alig = "-" + x_alig
            y_ind -= 1
        if alignment_matrix[x_ind][y_ind] == 0:
            break
    return (score, x_alig, y_alig)
#
#print(compute_local_alignment('AA', 'TAAT',test_, test2_))
