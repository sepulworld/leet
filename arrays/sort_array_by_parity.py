import pytest

def sortArrayByParity(A):
    positives = []
    negatives = []
    for i in A:
        if i % 2 == 0:
            positives.append(i)
        else:
            negatives.append(i)
    return positives + negatives

assert sortArrayByParity([3,1,2,4,100, 133, 23, 244]) == [2,4,100,244,3,1,133,23]