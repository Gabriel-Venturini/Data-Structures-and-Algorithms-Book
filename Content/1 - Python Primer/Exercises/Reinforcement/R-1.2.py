# Write a short Python function, is_even(k) that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.

def is_even(k):
    while k > 1:
        k -= 2
    if k == 0:
        return True
    return False

k = 100
result = is_even(k)
print(result)