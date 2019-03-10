# coding: utf-8
import pytest

"""Run with pytest -s locate_smallest_window_sorted.py to ignore stdout for logging/debugging"""

def locate_smallest_window_sorted(list):
    """Given an array of integers that are out of order, determine the bounds
    of the smallest window that must be sorted in order for the entire array
    to be sorted. For example, given [3, 7, 5, 6, 9], should return (1, 3)"""

    left, right = None, None
    sorted_list = sorted(list)
   
    print(f'The unsorted input list: {list}')
    print(f'The sorted input list: {sorted_list}')
    
    for i in range(len(list)):
        """based upon length of list, compare each index and find the left most index
        that doesn't match between unsorted and sorted"""
        print(f'Index {i}: Comparing {list[i]} with {sorted_list[i]}')
        if list[i] != sorted_list[i] and left is None:
            """Check if left is None,
            because we are doing a left to right traversal and will find left first."""
            print(f'Found left window index!: {list[i]} doesnt match {sorted_list[i]} and left window value not set yet, setting to {i}')
            left = i
        elif list[i] != sorted_list[i]:
            """No need to check it right is set, since we know we will find left first and right last"""
            print(f'Found right window index!: {list[i]} doesnt match {sorted_list[i]} and left window value not set yet, setting to {i}')
            right = i
        else:
            print(f'No window value at this index: {i}')
     
    return left, right
    
assert locate_smallest_window_sorted([9, 8, 13, 3, 14]) == (0, 3)
assert locate_smallest_window_sorted([4, 0, 11, 13, 5]) == (0, 4)
assert locate_smallest_window_sorted([1, 2, 0, 9, 13]) == (0, 2)
assert locate_smallest_window_sorted([1, 5, 13, 10, 6]) == (2, 4)
assert locate_smallest_window_sorted([4388, 18441, 17114, 21783, 7898, 3514, 9094, 10089, 26272, 1499, 20002, 26643, 2819, 24989, 15457, 29992, 4270, 12063, 16238, 15486, 20848, 28620, 26950, 24439, 17494, 14574, 28900, 28337, 27201, 27081]) == (0, 29)
