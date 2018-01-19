"""
Provide code and solution for Application 4
"""

DESKTOP = True

import math
import random
import urllib2

if DESKTOP:
    import matplotlib.pyplot as plt
    import alignments as student
else:
    import simpleplot
    import userXX_XXXXXXX as student


# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"


###############################################
# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    scoring_file = urllib2.urlopen(filename)
    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict


def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    protein_file = urllib2.urlopen(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq


def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib2.urlopen(filename)

    # read in files as string
    words = word_file.read()

    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print "Loaded a dictionary with", len(word_list), "words"
    return word_list

scoring_matrix = read_scoring_matrix(PAM50_URL)
human_protein = read_protein(HUMAN_EYELESS_URL)
fly_protein = read_protein(FRUITFLY_EYELESS_URL)
a_matrix = student.compute_alignment_matrix(human_protein, fly_protein, scoring_matrix, False)

alignment_1 = student.compute_local_alignment(human_protein, fly_protein, scoring_matrix, a_matrix)
print alignment_1
pax = read_protein(CONSENSUS_PAX_URL)
human_local = alignment_1[1]
fly_local = alignment_1[2]

human_local = human_local.replace("-", "")
fly_local = fly_local.replace("-", "")


def compute_percentage(local, pax):
    """
    Computes percentage of same characters in
    globabl alignment of local and pax
    """
    a_matrix = student.compute_alignment_matrix(local,
                                                pax, scoring_matrix, True)
    alig = student.compute_global_alignment(local,
                                            pax, scoring_matrix, a_matrix)
    total = 0
    same = 0
    for index in range(len(alig[1])):
        total += 1
        if alig[1][index] == alig[2][index]:
            same +=1
    print total
    return float(same) / total

print compute_percentage(human_local, pax)
print compute_percentage(fly_local, pax)

# (875, 'HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEK-QQ', 'HSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQ')
# 133 position, 23 sybols

# 1/23 for sybols to be exactly the same

print (1.0 / 23) ** 70
