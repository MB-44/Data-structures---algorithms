"""
dynamic programming is an algorithmic technique for solving and optimisation problem
by breaking it down into simpler subproblems and utilising the fact that the optimal solution
to the overall problem depends upon the optimal solution to its subproblems.
"""


# this solution will be like o(2^n)
def fib(n):
    if n<2:
        return n 
    return fib(n-1) + fib(n-2)

print(fib(3))


# O(n)
# optimal solution for the fibonaci sequence
def fibMemo(n, cache={}):
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    cache[n] = fibMemo(n - 1, cache) + fibMemo(n - 2, cache)
    return cache[n]