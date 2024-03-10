# Write a short Python program that takes as input three integers, a, b and c,
# from the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like "a + b = c", "a = b - c" or "a * b = c".

a = int(input())
b = int(input())
c = int(input())

if a + b == c:
    print("a + b = c")
elif b - c == a:
    print("a = b - c")
elif a * b == c:
    print("a * b = c")
else:
    print("No arithmetic operation available.")