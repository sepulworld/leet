import pytest

"""Run with pytest -s insert_sort.py to ignore stdout for logging/debugging
   Using input() to pause and observe where you are in algo process"""

def insert_sort(array):
    """Implement the insert based sort algo"""
    print(f'Looping over each index vaule of the input array, starting with one and ending with {len(array)}')

    for index in range(1, len(array)):
        input(f'Working on {index} with value {array[index]}')
        while index > 0 and array[index - 1] > array[index]:
            print(f'In loop because {index} > 0 and {array[index - 1]} > {array[index]}')
            print(f'swapping {array[index]}, {array[index - 1]}')
            array[index], array[index - 1] = array[index - 1], array[index]
            input(f'subtracing 1 from {index} giving us previous index to now validate {index - 1}')
            index -= 1
        else:
            print(f'Exiting while loop because {index} > 0 and {array[index - 1]} > {array[index]} is False')
            print(f'Array sort process is at {array}...')
    
    print(f'Finished sort of array!')
    return array


assert insert_sort([2, 17,112, 1, 0, 6,10]) == [0, 1, 2, 6, 10, 17, 112]
assert insert_sort([1, 10000, 4, 1, 0, 2]) == [0, 1, 1, 2, 4, 10000]