import pytest 

fib_seq = {}

def fib(self, N: int) -> int:

    # deal with 1
    if (N == 1):
        fib_seq[N] = 1
    # deal with 0
    elif (N == 0):
        fib_seq[N] = 0
    # deal with N if already in dictionary hash and return
    elif (N in self.fib_seq):
        return fib_seq[N]
    # else add N via recursive call to function, adding 2 prior iteration results to N in hash
    else:
        fib_seq[N] = fib(N - 1 ) + fib(N - 2)
        
    return fib_seq[N]