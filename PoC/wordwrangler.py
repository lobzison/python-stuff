"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided
import math

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    res = []
    index = 0
    # empty and one elements lists can't contain duplicates
    if len(list1) <= 1:
        res = list1
    else:
        # first element in list of len > 1 is unique
        res.append(list1[0])
        while index < len(list1) - 1:
            if list1[index] != list1[index + 1]:
                res.append(list1[index + 1])
                index += 1
            else:
                index += 1
    return res


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    index_1 = 0
    index_2 = 0
    res = []
    # intersect with [] is []
    if not (list1 == [] or list2 == []):
        while index_1 < len(list1) and index_2 < len(list2):
            if list1[index_1] == list2[index_2]:
                res.append(list1[index_1])
                index_1 += 1
                index_2 += 1
            elif list1[index_1] > list2[index_2]:
                index_2 += 1
            else:
                index_1 += 1
    return res

# Functions to perform merge sort


def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    res = []
    if (list1 == [] or list2 == []):
        return list1 + list2
    else:
        index_1 = 0
        index_2 = 0
        while index_1 < len(list1) and index_2 < len(list2):
            if list1[index_1] == list2[index_2]:
                res.append(list1[index_1])
                res.append(list2[index_2])
                index_1 += 1
                index_2 += 1
            elif list1[index_1] > list2[index_2]:
                res.append(list2[index_2])
                index_2 += 1
            else:
                res.append(list1[index_1])
                index_1 += 1

        if len(list1) >= index_1:
            res += list1[index_1:]
        if len(list2) >= index_2:
            res += list2[index_2:]
    return res


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        return list1
    else:
        mid_index = int(math.ceil((len(list1) / 2)))
        first_list, second_list = list1[:mid_index], list1[mid_index:]
        first_list, second_list = merge_sort(
            first_list), merge_sort(second_list)
        return merge(first_list, second_list)

# Function to generate all strings for the word wrangler game


def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """

    if len(word) == 0:
        return [""]
    if len(word) == 1:
        return ["", word]
    # splitting the string into first character and rest
    # generate all perms on rest
    # for each perm put first letter in every possible plase
    first = word[:1]
    rest = word[1:]
    rest_strings = gen_all_strings(rest)
    new_strings = []
    for string in rest_strings:
        for index in range(len(string) + 1):
            new_string = string[:index] + first + string[index:]
            new_strings.append(new_string)
    return new_strings + rest_strings

# Function to load words from a file


def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)


# Uncomment when you are ready to try the game
# run()
#tes_list1 = []
#tes_list2 = [3]
#tes_list3 = [1,2]
#tes_list4 = [1,2,3,4,5,6]
#tes_list5 = [1,2,3,4,5,5]
#tes_list6 = [1,1,3,4,5,6]
#tes_list7 = [1,2,3,3,3,3]
#
#
#test_list1 = []
#test_list2 = [1, 19, 20, 21]
#test_list3 = [19, 38, 98]
#test_list4 = [1, 19, 19,  20, 21]
#test_list5 = [19, 19, 38, 98]
#test_list5 = [3, 4, 7, 30]
#
#unsorted_list1 = [6, 1, 25, 12, 4, 1, 2, 90, 12]
#
# print remove_duplicates(tes_list7)
#
# print intersect(test_list3, test_list4)
#
# print merge(test_list2, test_list5)
#
# print merge_sort([2, 3, 1])
# print len("a")
#print gen_all_strings("abc")
