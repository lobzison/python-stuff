"""
Leap game
"""

def is_goal_reachable_max(leap_list, start_index, max_leaps):
    """ 
    Determines whether goal can be reached in at most max_leaps leaps.

    Arguments:
    leap_list - the leap list game board.
    start_index - the starting index of the player.
    max_leaps - the most number of leaps allowed before the player loses.

    Returns:
    True if goal is reachable in max_leap or less leaps.  False if goal is not reachable in max_leap or fewer leaps.
    """
    if leap_list[start_index] == 0:
        return True
    if max_leaps == 0:
        return False
    step_left = start_index - leap_list[start_index]
    step_right = start_index + leap_list[start_index]
    left, right = False, False
    if step_left >= 0:
        left = is_goal_reachable_max(leap_list, step_left, max_leaps - 1)
    if step_right < len(leap_list):
        right = is_goal_reachable_max(leap_list, step_right, max_leaps - 1)
    return left or right

print is_goal_reachable_max([1, 2, 3, 3, 3, 1, 0], 0, 3)
#True
print is_goal_reachable_max([1, 2, 3, 3, 3, 1, 0], 0, 2)
#False
print is_goal_reachable_max([1, 2, 3, 3, 3, 1, 0], 4, 3)
#True
print is_goal_reachable_max([1, 2, 3, 3, 3, 1, 0], 4, 2)
#False
print is_goal_reachable_max([2, 1, 2, 2, 2, 0], 1, 5)
#False
print is_goal_reachable_max([2, 1, 2, 2, 2, 0], 3, 1)
#True


def is_goal_reachable(leap_list, start_index):
    """ 
    Determines whether goal can be reached in any number of leaps.

    Arguments:
    leap_list - the leap list game board.
    start_index - the starting index of the player.

    Returns:
    True if goal is reachable.  False if goal is not reachable.
    """
    def is_goal_reachable_mem(leap_list, start_index, visited_indexes):
        if leap_list[start_index] == 0:
            return True
        visited_indexes.add(start_index)
        step_left = start_index - leap_list[start_index]
        step_right = start_index + leap_list[start_index]
        left, right = False, False
        if step_left >= 0 and step_left not in visited_indexes:
            left = is_goal_reachable_mem(leap_list, step_left, visited_indexes)
        if step_right < len(leap_list) and step_right not in visited_indexes:
            right = is_goal_reachable_mem(leap_list, step_right, visited_indexes)
        return left or right 
    visited = set([])
    return is_goal_reachable_mem(leap_list, start_index, visited)
    
print "----------"
print is_goal_reachable([1, 2, 3, 3, 3, 1, 0], 0)
#True
print is_goal_reachable([1, 2, 3, 3, 3, 1, 0], 4)
#True
print is_goal_reachable([2, 1, 2, 2, 2, 0], 1)
#False
print is_goal_reachable([2, 1, 2, 2, 2, 0], 3)
#True
print is_goal_reachable([3, 6, 4, 1, 3, 4, 2, 5, 3, 0], 0)
#True
    
