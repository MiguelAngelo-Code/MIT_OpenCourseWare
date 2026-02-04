# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letters in secret_word:
        if letters not in letters_guessed:
            return False
        
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
        if char in letters_guessed:
            guessed_word.append(char)
        else: 
            guessed_word.append("_ ")

    return guessed_word
                



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # Create char list of alphabet
    alphabet = []
    for i in range(97, 123):
        alphabet.append(chr(i))

    letters_available = []
    for char in alphabet:
        if char not in letters_guessed:
            letters_available.append(char)
    
    return letters_available
            
def hangman(secret_word):
    
    # Get secret word
    secret_word = choose_word(wordlist)

    # Iniciate guesses left and list to store guessed letters
    guesses_left = 6
    letters_guessed = []

    # Spacer
    print("--------------------------------")
    
    # Print starting sequence to terminal
    print(f"I am thinking of a", len(secret_word), "letter word")

    # Spacer
    print("--------------------------------")

    # Iniciate loop to itirate untill 6 guesses have been made
    while True:
        
        #prints guesses left and availabel words
        print(f"You have", guesses_left, "guesses left")
        print(f"Letters available:", "".join(get_available_letters(letters_guessed)))

        # Get user input and re-promt if user inputs more than 1 letter
        guess = input("Guess 1 letter: ").lower()
        while (len(guess) != 1 or not guess.isalpha()):
          print("Error, please guess 1 letter at a time")
          guess = input("Guess 1 letter: ").lower()

        # Appends guess to letters guessed
        letters_guessed.append(guess)
        
        # Checks if guess in secret word
        if guess in secret_word:
            print("Correct!")
        else:
            print("Incorrect!")
            guesses_left -= 1

        # Display guessed word & print spacer
        print("".join(get_guessed_word(secret_word, letters_guessed)))
        print("-----------------------")

        # Checks for win loss conditions
        if (is_word_guessed(secret_word, letters_guessed)):
            print("Congratulations!!! You guessed the word")
            print("Score:", (guesses_left * len(secret_word)))
            return True
        
        if guesses_left < 1:
            print("Sorry! You lose! :(")
            print(f"The Word was:", secret_word)
            return True
        
      
        
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # Strips spaces from my word
    my_word = my_word.strip()
    my_word = my_word.replace(" ", "")

    # Check word lenth
    if  len(my_word) != len(other_word):
        return False
    else:
        # loop checks for mismatches in words
        for i in range(len(my_word)):
            # If my_word[i] alpha and not match other word[i] return flase
            if my_word[i].isalpha():
               if my_word[i] != other_word[i]:
                   return False
            # if word not alpha and if other word[i] in myword return false
            else:
                if other_word[i] in my_word:
                    return False
    
    # Returns true if no missmatch found       
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    print("Possible matches: ")

    for word in wordlist: 
        if match_with_gaps(my_word, word) == True: 
            print(word)
    
    return None


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    # Get secret word
    # secret_word = choose_word(wordlist)
    secret_word = "ample"

    # Iniciate guesses left and list to store guessed letters
    guesses_left = 6
    letters_guessed = []

    # Spacer
    print("--------------------------------")
    
    # Print starting sequence to terminal
    print(f"I am thinking of a", len(secret_word), "letter word")

    # Spacer
    print("--------------------------------")

    # Iniciate loop to itirate untill 6 guesses have been made
    while True:
        
        #prints guesses left and availabel words
        print(f"You have", guesses_left, "guesses left")
        print(f"Letters available:", "".join(get_available_letters(letters_guessed)))

        # Get user input
        guess = input("Guess 1 letter: ")

        # User requests hint:
        if guess == "*":
            show_possible_matches("".join(get_guessed_word(secret_word, letters_guessed)))#passing through list not string, may be issue. 
            
        # If user makes guess
        else:
            guess = guess.lower()
            #checks for valid input
            while (len(guess) != 1 or not guess.isalpha()):
              print("Error, please guess 1 letter at a time")
              guess = input("Guess 1 letter: ").lower()

            # Appends guess to letters guessed
            letters_guessed.append(guess)
            
            # Checks if guess in secret word
            if guess in secret_word:
                print("Correct!")
            else:
                print("Incorrect!")
                guesses_left -= 1

            # Display guessed word & print spacer
            print("".join(get_guessed_word(secret_word, letters_guessed)))
            print("-----------------------")

            # Checks for win loss conditions
            if (is_word_guessed(secret_word, letters_guessed)):
                print("Congratulations!!! You guessed the word")
                print("Score:", (guesses_left * len(secret_word)))
                return True
            
            if guesses_left < 1:
                print("Sorry! You lose! :(")
                print(f"The Word was:", secret_word)
                return True
            



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
