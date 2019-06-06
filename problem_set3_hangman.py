# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words1.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    answer = True
    for i in secretWord:
        if i not in lettersGuessed:
            answer = False
            return answer
    return answer


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    answer = ''
    for i in secretWord:
        if i not in lettersGuessed:
            answer = answer + '-'
        else:
            answer = answer + i
    return answer



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in lettersGuessed:
        letters.remove(i)
    return ''.join(letters)
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    mistakes = 0
    secret_word = secretWord
    letters_guessed = []
    length = len(secret_word) 
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(length) + " letters long.")
    print("----------------")
    game_over = False
    while not game_over:
        if mistakes == 8:
            print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
            game_over = True
            return
        print("You have " + str(8 - mistakes) + " guesses left.")
        print("Available Letters: " + getAvailableLetters(letters_guessed))
        guess = input('Please guess a letter:')
        guess_lower = guess.lower()
        if guess_lower in letters_guessed:
            print("Oops! You've already guessed that letter: " +  getGuessedWord(secret_word, letters_guessed))
            print("----------------")
        elif guess_lower in secret_word:
            letters_guessed.append(guess_lower)
            print("Good guess: " + getGuessedWord(secret_word, letters_guessed))
            print("----------------")
            if isWordGuessed(secret_word, letters_guessed):
                print("Congratulations, you won!")
                game_over = True
        else:
            letters_guessed.append(guess_lower)
            print("Oops! That letter is not in my word: " + getGuessedWord(secret_word, letters_guessed))
            print("----------------")
            mistakes += 1




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
