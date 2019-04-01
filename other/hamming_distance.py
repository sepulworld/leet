import pytest

def hammingDistance(x: int, y: int):
    """https://leetcode.com/problems/hamming-distance/"""

    hamming_distance = 0
    
    binary_x = f'{x:064b}'
    binary_y = f'{y:064b}'
    
    for index in range(len(binary_x)):
        if binary_x[index] != binary_y[index]:
            hamming_distance += 1
    
    return hamming_distance

assert hammingDistance(1, 4) == "2"
assert hammingDistance(297630147, 147274294) == "17"
