import pytest

def selfDividingNumbers(left: int, right: int):
    """https://leetcode.com/problems/self-dividing-numbers/"""

    self_dividing_numbers = []
    
    for i in range(left, right + 1):
        if test_self_divisible(i) == True:
            self_dividing_numbers.append(i)

    return self_dividing_numbers

def test_self_divisible(number: int):
    self_dividing = True

    for digit in str(number):
        if int(digit) == 0:
            self_dividing = False
            return self_dividing
        elif number % int(digit) != 0:
            self_dividing = False
    
    return self_dividing


assert selfDividingNumbers(1, 22) == [1,2,3,4,5,6,7,8,9,11,12,15,22]
