import pytest

def diStringMatch(S):
    results = []
    j = len(S)
    a = 0
    
    for i in S:
        if i == "I":
            results.append(a)
            a += 1
        else:
            results.append(j)
            j = j - 1
            
    results.append(j if S[-1] == "D" else a)
    
    return results

assert diStringMatch("IDID") == [0,4,1,3,2]