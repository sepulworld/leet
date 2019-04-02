import pytest

def arrayPairSum(nums):
    """https://leetcode.com/problems/array-partition-i/submissions/"""

    nums.sort()
    max_sum = 0

    while nums:
        max_sum += min(nums.pop(), nums.pop())
    
    return max_sum

assert arrayPairSum([1, 4, 3, 2, 6, 9, 20, 22, 77, 99]) == 107
