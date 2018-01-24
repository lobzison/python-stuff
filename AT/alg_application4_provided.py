"""
Provide code and solution for Application 4
"""

DESKTOP = True

import math
import random
import urllib2
import string

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
a_matrix = student.compute_alignment_matrix(
    human_protein, fly_protein, scoring_matrix, False)

alignment_1 = student.compute_local_alignment(
    human_protein, fly_protein, scoring_matrix, a_matrix)
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
            same += 1
    print same
    print total
    return float(same) / total


print compute_percentage(human_local, pax)
print compute_percentage(fly_local, pax)

# (875, 'HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEK-QQ', 'HSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQ')
# 133 position, 23 sybols

# 1/23 for sybols to be exactly the same

print (1.0 / 23) ** 70


def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    """
    Generates unnormalized distribution of permutations
    of maximum scores of local gene alignments
    """
    scoring_distribution = {}
    for _ in range(num_trials):
        print("Start")
        y_lst = list(seq_y)
        random.shuffle(y_lst)
        rand_y = ''.join(y_lst)
        print("shuffled")
        alignment_matrix = student.compute_alignment_matrix(
            seq_x, rand_y, scoring_matrix, False)
        print("alig_matrix")
        permutation_score = student.compute_local_alignment(
            seq_x, rand_y, scoring_matrix, alignment_matrix)[0]
        print("permutation score")
        if scoring_distribution.get(permutation_score) is None:
            scoring_distribution[permutation_score] = 1
        else:
            scoring_distribution[permutation_score] += 1
        print("added")
        print _
    return scoring_distribution


null_distibution = {37: 1, 38: 1, 39: 4, 40: 13, 41: 14, 42: 19, 43: 31, 44: 37, 45: 60, 46: 51, 47: 67, 48: 69, 49: 60, 50: 56, 51: 65, 52: 62, 53: 48, 54: 55, 55: 45, 56: 32, 57: 34,
                    58: 27, 59: 22, 60: 17, 61: 16, 62: 20, 63: 16, 64: 10, 65: 11, 66: 8, 67: 3, 68: 8, 69: 3, 70: 1, 71: 3, 72: 2, 73: 1, 74: 1, 75: 1, 77: 1, 79: 1, 84: 1, 86: 1, 87: 1, 89: 1}


def show_hist(dist):
    """
    Plots a histogramm of distribution
    """
    total = sum(dist.values())
    weighted_dist = {key: float(val) / total for (key, val)
                     in zip(dist.keys(), dist.values())}
    plt.bar(weighted_dist.keys(), weighted_dist.values())
    plt.xlabel("Maximum score in permutation matrix")
    plt.ylabel("Normalized appearence")
    plt.title("Distirbution of maximum scores in permutation matrix"
              + " for 1000 attempst, radomizing oreder in human sequence")
    plt.show()

    return total

def z_score(dist, num):
    """
    Calculates z score for distribution
    """
    mu = float(sum((key * val for (key, val)
                    in zip(dist.keys(),
                           dist.values())))) / 1000

    # print show_hist(dist)
    print "mean is: " + str(mu)
    sigma = math.sqrt(float(sum(((key - mu) ** 2) * val for (key, val)
                                in zip(dist.keys(),
                                       dist.values()))) / 1000)

    print "standart is: " + str(sigma)
    print "tripple st dev:" + str(mu + 3 * sigma)
    return (num - mu) / sigma

print z_score(null_distibution, 875)

words = read_words(WORD_LIST_URL)
def check_spelling(checked_word, dist, word_list):
    """
    Simple and stupid autocorrect
    """
    result = set([])
    scoring_matrix = student.build_scoring_matrix(set(list(string.ascii_lowercase)), 2, 1, 0)
    set_words = set(word_list)
    for word in set_words:
        alignment_matrix = student.compute_alignment_matrix(
            word, checked_word, scoring_matrix, True)
        permutation_score = student.compute_global_alignment(
            word, checked_word, scoring_matrix, alignment_matrix)[0]
        distance = len(checked_word) + len(word) - permutation_score
        if distance <= dist:
            result.add(word)
    return result

print check_spelling("humble", 1, words)
print check_spelling("firefly", 2, words)
