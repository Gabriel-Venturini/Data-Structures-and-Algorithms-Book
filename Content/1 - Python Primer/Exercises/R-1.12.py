# Python's random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range. Using only the randrage function, implement your own version of the choice function.

import random

def randChoice(sequence):
    big = max(sequence)
    small = min(sequence)
    return random.randrange(small, big)


arr = [1,2,3,4,5,6]

randomValue = randChoice(arr)
print(randomValue)