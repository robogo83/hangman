import random

word_list = ['banana', 'apple', 'pear', 'orange', 'grapes']


class Hangman:
    '''
    Crates an object to start hangman game. When the object is created a random word is selected from the word_list.
    list_of_guesses object is created to store the user's guesses
    Parameters
    ----------
    word_list: list of words to be guessed 
    num_lives: default 5

    Methods
    -------
    check_guess: return None; checks if the guess is valid and updates the values
    ask_for_input: return None; asks for a letter from the user and calls check_guess method
    '''

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(letter for letter in self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        Return: None
        Checks if the user's value is valid and updates following variables:
        num_letters: if the guess is correct it decreases the number of letters to be guessed
        num_lives: if the guess is not correct it decreases the number of lives
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[index] = guess
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        '''
        Return: None
        Asks the user for a letter and calls the check_guess method to
        check the input and update game variablex.
        '''
        while True:
            guess = input("Guess a letter: ")
            if len(guess) > 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess.isalpha() == False:
                print("Invalid character. Only letters are allowed.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    '''
    This funciton control the flow game using while loop.
    The loop checks for num_lives, num_letters left and evaluates at what stage of the
    game the user is. This function creates Hangman objecct and calls the ask_for_input
    method so that the game can start.
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print(f"Welcome to hangman game. Your word: {game.word_guessed}")
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break


if __name__ == '__main__':
    play_game(word_list)
