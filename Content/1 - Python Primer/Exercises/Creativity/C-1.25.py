# Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For example,
# if gievn the string "Let's try, Mike.", this function would return
# "Lets try Mike"

def noPunctuation(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    newS = s
    for letter in s:
        if letter.lower() not in alphabet:
            newS = newS.replace(str(letter), '')
            print(letter)

    return newS

s = "Let's try, Mike."
newString = noPunctuation(s)
print(newString)
