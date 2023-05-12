"""
Configurations

Control variations of the game Wordle
"""

# number of guesses
NGUESSES = 5

# valid word length
NWORDLEN = 5

# set of symbols that can be used for a tile
CHOICES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
UNKNOWN = "."

DICTION = []
with open("word_dictionary/wordlist_five.txt", 'r') as fp:
    for num, line in enumerate(fp):
        if not line.isspace():
            DICTION.append(line.strip())
