import pytest

def numJewelsInStones(J: str, S: str) -> int:
    my_jewels = 0

    for i in S:
        if i in J:
            my_jewels += 1

    return my_jewels

assert numJewelsInStones("aAXyzx", "aAAAAXlmz") == 7
assert numJewelsInStones("aA", "aAAAAXlmz") == 5
