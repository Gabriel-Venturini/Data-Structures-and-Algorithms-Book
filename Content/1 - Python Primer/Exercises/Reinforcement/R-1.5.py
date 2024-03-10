# Give a single command that computes the sum from Exercise R-1.4, relying on Python's comprehension syntax and the built-in function.

def sqrtSum(n):
    arr = [k*k for k in range(1, n)]
    total = sum(arr)
    return total

n = 5
total = sqrtSum(n)
print(total)