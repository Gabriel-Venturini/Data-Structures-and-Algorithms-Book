# Write a short Python function that counts the number of vowels in a given string

def getVowels(s):
    vowels = 'aeiou'
    counter = 0

    for letter in s:
        if letter in vowels:
            counter += 1
    return counter

s = 'gabriel'
vowelscount = getVowels(s)
print(f'There is {vowelscount} vowels in the sentence provided.')