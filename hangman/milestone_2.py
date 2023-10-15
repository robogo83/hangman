import random

word_list = ['banana', 'apple', 'pear', 'orange', 'grapes']

word = random.choice(word_list)

guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops that is not a valid input')
