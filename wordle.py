"""
simple wordle game
"""

import wordle_gboard as wgb
from wordle_config import NWORDLEN

def main():
    # test import
    b = wgb.Board()
    #b.print_board()

    # pick target word
    # randomize? for now just assign
    target = "wants"

    # while remaining guess available or guesses target
    while True:
        # ask user for guess
        guess = input("guess a word (press enter to exit): ")
        if guess == '':
            break

        print(f'word guessed: {guess}')

        # check if guess valid
        if len(guess) != NWORDLEN:
            print(f'word must be of length {NWORDLEN}')
        
        print(f'target word: {target}')
        if guess is target:
            print(f'solved')
            break


        # check if guess within dictionary
        

        # add guess to board


        # add corresponding colors


        # print out board

if __name__=="__main__":
    main()
