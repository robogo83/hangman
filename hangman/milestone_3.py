import random

word_list = ['banana', 'apple', 'pear', 'orange', 'grapes']
# selecting a random word from word_list
word = random.choice(word_list)

# check the chosen word for testing purposes. This will be removed
print(word)


def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        elif len(guess) > 1:
            print("Please enter only one letter")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)


ask_for_input()
