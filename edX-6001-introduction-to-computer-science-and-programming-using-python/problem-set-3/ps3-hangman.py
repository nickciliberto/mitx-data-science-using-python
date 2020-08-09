# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

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
    
    counter = 0
    
    #iterates over letters in secretWord
    for letter in secretWord:
        #counts number of letters that have been correctly guessed 
        if letter in lettersGuessed:
            counter += 1
    #returns True if all letters have been guessed
    if counter == len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    progress = ''
    
    #iterates over letters in secretWord
    for letter in secretWord:
        #if letter has been guessed, add to progress string, otherwise add
        #underscore
        if letter in lettersGuessed:
            progress = progress + letter
        else:
            progress = progress + ' _ '
    return progress
        



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: string, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters = ''
    
    #import string to generate alphabetical string of lowercase letters
    import string
    
    #iterate over string of lowercase letters
    for letter in string.ascii_lowercase:
        #add all unguessed letters to string of available letters
        if letter not in lettersGuessed:
            available_letters = available_letters + letter
    
    return available_letters
    
#hangman game
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
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('-----------')
    guesses_remaining = 8
    lettersGuessed = ''

    #indicates whether user has correctly guessed word, True if user has won
    guessed_word = False
    
    #while user hasn't guessed word and hasn't run out of guesses
    while not guessed_word and guesses_remaining > 0: 
        
        #turned to True if guess is a letter that has nto already been guessed
        validGuess = False
        #ensures that we receive a valid guess before continuing outer loop
        while not validGuess:
            available_letters = getAvailableLetters(lettersGuessed)
            #tells user how many guesses they have left
            print('You have', guesses_remaining, 'guesses left')
            #tells user letters that haven't been guessed
            print('Available letters:', available_letters)
            #converts any letter input to lowercase
            guess = input('Please guess a letter: ').lower()
            #if user has already guessed letter, repeat loop, otherwise move on
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter:", \
                      getGuessedWord(secretWord, lettersGuessed))
                print('-----------')
            else:
                validGuess = True    
        
        #add letter to list of letters guessed
        lettersGuessed = lettersGuessed + guess
        #if letter is in word, good guess, show progress
        if guess in secretWord:
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
        #if letter is not in word, decrease num of remaining guesses
        else:
            print('Oops! That letter is not in my word:', \
                  getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
            guesses_remaining -= 1
        #helper function, returns True if word has been guessed
        guessed_word = isWordGuessed(secretWord, lettersGuessed)
        #break if word has been guessed, user wins
        if guessed_word:
            print('Congratulations! You won!')
            break
        #break if user runs out of guesses, game over
        if guesses_remaining <= 0:
            print('Sorry, you ran out of guesses. The word was', secretWord)
            break

#generates random word from wordlist txt file
secretWord = chooseWord(wordlist).lower()

#runs game
hangman(secretWord)
