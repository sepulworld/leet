import pytest
import collections

def commonChars(A):
    """https://leetcode.com/problems/find-common-characters/"""

    res = collections.Counter(A[0])
    print(f'collection of A input: {res}')
    
    for a in A:
        print(f'working on {a}')
        res &= collections.Counter(a)
        print(res)
        
    return list(res.elements())

assert commonChars(["bella","label","roller"]) == ["e", "l", "l"]