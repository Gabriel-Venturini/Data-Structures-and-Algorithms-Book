# Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smallers then n.

def sqrtSum(n):
    sum = 0
    for i in range(1, n):
        sum += i * i
    
    return sum

n = 5
total = sqrtSum(n)
print(total)