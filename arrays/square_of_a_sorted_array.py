import pytest


def sortedSquares(A):
    squared_ints = []

    for i in A:
        squared_int = i**2
        squared_ints.append(squared_int)
    
    sorted_result = squared_ints.sort()

    return sorted_result

assert sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
