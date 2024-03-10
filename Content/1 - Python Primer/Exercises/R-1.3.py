# Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.

def minmax(data):
    # formula: (a + b + abs(a - b)) / 2 biggest
    # formula: (a + b - abs(a - b)) / 2 smallest

    a, b, c = data[0], data[1], data[2]

    biggest = (a + b + abs(a - b)) / 2
    biggest = (biggest + c + abs(biggest - c)) / 2

    smallest = (a + b - abs(a - b)) / 2
    smallest = (smallest + c - abs(smallest - c)) / 2

    return f'Biggest: {biggest} and Smallest: {smallest}'

data = (12, 1, 5)
test = minmax(data)
print(test)