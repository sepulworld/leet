import pytest

def singleNumber(nums):
    """https://leetcode.com/problems/single-number/"""
    counts = {}
    
    for i in nums:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    
    for key, val in counts.items():
        if val == 1:
            return key

assert singleNumber([2,2,1]) == 1
