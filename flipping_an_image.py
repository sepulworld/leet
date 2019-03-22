import pytest

def flipAndInvertImage(A):
    for i in A:
        # Reverse the image
        i.reverse()

        # Flip the image
        for index, num in enumerate(i):
            if num == 1:
                i[index] = 0
            else:
                i[index] = 1
    return A

assert flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 