import pytest

def repeatedNTimes(A):
    for num in A:
        if A.count(num) >= 2:
            return num

assert repeatedNTimes([5,1,5,2,5,3,5,4]) == 5
