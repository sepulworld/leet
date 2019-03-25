import pytest

def judgeCircle(moves):
    """https://leetcode.com/problems/robot-return-to-origin/"""

    position = { "x": 0, "y": 0}
    
    for i in moves:
        if i == "R":
            position["y"] = position["y"] + 1
        if i == "L":
            position["y"] = position["y"] - 1
        if i == "U":
            position["x"] = position["x"] + 1
        if i == "D":
            position["x"] = position["x"] - 1
    
    if position == { "x": 0, "y": 0}:
        return True
    else:
        return False

assert judgeCircle("UD") == True 
assert judgeCircle("UDLL") == False
