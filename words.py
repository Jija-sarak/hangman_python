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
    word_list = line.split()
    print("  ", len(word_list), "words loaded.\n\n")
    return word_list
def choose_word():
    """
    word_list (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(word_list)

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

