# Write a Python program that repeatedly reads lines from standard input until
# an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing CTRL + D).

while True:
    try:
        user = input('type: ')
    except EOFError as err:
        print('EOFError: ', err)