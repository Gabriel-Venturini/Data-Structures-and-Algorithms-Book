# Give a single command that computes the sum from Exercise R-1.6, relying on Python's comprehension syntax and the built-in sum function.

def sumOddSquares(n):
    arr = [k*k for k in range(1, n, 2)]
    total = sum(arr)
    return total

n = 7
total = sumOddSquares(n)
print(total)