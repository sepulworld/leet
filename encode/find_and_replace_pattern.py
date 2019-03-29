import pytest

def findAndReplacePattern(words, pattern):
    """https://leetcode.com/problems/find-and-replace-pattern/"""
    
    out = []
    p = _convert(pattern)
    print(f'pattern encodes to: {p}')
    for w in words:
        print(f'encoded patter for word: {w} = {_convert(w)}')
        if p == _convert(w):
            out.append(w)

    return out

def _convert(word):
    encode = {}
    count = 0
    out = ''
    for char in word:
        if char not in encode:
            encode[char] = str(count)
            out += encode[char]
            count += 1
        else:
            out += encode[char]

    return out

assert findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb") == ["mee","aqq"]