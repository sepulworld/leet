import pytest

def maxIncreaseKeepingSkyline(grid):
    max_left_right = []
    max_top_bottom = []
    max_total_height_increase = 0
    
    for index in range(len(grid)):
        top_down = []
        for block in grid:
            top_down.append(block[index])
        max_top_bottom.append(max(top_down))
        
    for block in grid:
        max_left_right.append(max(block))
            
    for block_index, block in enumerate(grid):
        for building_index, building in enumerate(block):
            new_height = min([max_left_right[block_index], max_top_bottom[building_index]])
            max_total_height_increase += new_height - block[building_index]
            
    return max_total_height_increase

assert maxIncreaseKeepingSkyline([[3, 0, 8, 4],[2, 4, 5, 7],[9, 2, 6, 3],[0, 3, 1, 0]]) == 35
