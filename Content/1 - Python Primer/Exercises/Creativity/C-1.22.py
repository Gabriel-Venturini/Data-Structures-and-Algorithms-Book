# Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is,
# it returns an array c of length n such that c[i] = a[i] * b[i], for i = 0, ..., n-1.

# Function
def dotProduct(a, b, length):
    newArr = []
    for i in range(0, length): # this way I can use c[i]
        newArr.append(0)

    for i in range(0, length):
        newArr[i] = a[i] * b[i]

    return newArr

# Executes the code here
arrA = [2, 4, 6, 3]
arrB = [5, 10, 3, 20]
length = len(arrA)
arrC = dotProduct(arrA, arrB, length)
print(arrC)