import pytest

def multiply_for_product(list):
    """Allowing for division, get product of all other elements, input list"""
   
    result = 1
    for num in list:
        result = result * num
    product_of_all = []
    for num in list:
        product_of_all.append(int(result / num))
    
    return product_of_all

assert multiply_for_product([1,2,3,4,5]) == [120, 60, 40, 30, 24]
