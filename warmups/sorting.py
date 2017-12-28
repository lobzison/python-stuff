def bubble_sort(input_list):
    output_list = list(input_list)
    while True:
	    is_moved = False
        for idx in range(len(output_list)) - 1:
            if output_list[idx] > output_list[idx + 1]:
			    output_list[idx], output_list[idx + 1] = output_list[idx + 1], output_list[idx]
				is_moved = True
		if not is_moved:
		    break
	return output_list
	
	
def merge_sort(i_list):
    """Takes input list and returns copy of sorted list"""
    def merge(list1, list2):
	    """ Merges two sorted lists"""
	    if  not list1 or not list2:
		    return list1 + list2
	    idx1 = 0
		idx2 = 0
		res = []
		while idx1 < len(list1) and idx2 < len(list2):
		    if list1[idx1] == list2[idx2]:
			    res.append(list1[idx1])
				res.append(list2[idx2])
				idx1 += 1
				idx2 += 1
			elif list1[idx1] > list2[idx2]:
			    res.append(list2[idx2])
				idx2 +=1
		    else:
			    res.append(list1[idx1])
				idx1 +=1
		if idx1 < len(list1):
			res += list1[idx1:]
		if idx2 < len(list2):
			res += list2[idx2:]
		return res
		
	if len(i_list) <= 1:
	    return list(i_list)
    else:
	    mid_idx = len(i_list) // 2
	    first_part, second_part = i_list[:mid_idx], i_list[mid_idx:]
		first_part, second_part = merge_sort(first_part), merge_sort(second_part)
		return merge(first_part, second_part)
		
		
		
import random
def quick_sort(i_list):
    """Return a copy of i_list sorted in ascending way."""
    if len(i_list) < 1:
        return list(i_list)
    else:
        pivot_i = random.randrange(len(i_list))
        pivot_v = i_list[pivot_i]
        low, pivot, high = [],[],[]
        for item in i_list:
            if item == pivot_v:
                pivot.append(item)
            elif item > pivot_v:
                high.append(item)
            else:
                low.append(item)
        return quick_sort(low) + pivot + quick_sort(high)
