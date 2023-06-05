"""
simple wordle game
"""

#import random
import wordle_gboard as wgb
from wordle_config import NWORDLEN, NGUESSES, DICTION, TARGET

def main():
    
    # create game board
    b = wgb.Board()
    b.print_board()
    #b.print_choices()

    # print TARGET word for debugging purpose
    #print(f'Goal: {TARGET}')
    while True:
        game_mode = input("\nComputer Solve? (y/n): ")
        
        if not game_mode:
            print('Exiting Program')
            exit()
        elif game_mode.lower() == 'y':
            b.solve()
            exit()
        elif game_mode.lower() == 'n':
            break
        else:
            print('\ninvalid input')
    

    # initializing trackers for length of game
    correct_guess = False
    counter = 0

    # while remaining guess available or if target is guessed
    while not correct_guess:
        
        # initialize
        invalid_guess = True
        
        # ask user for a valid guess
        while invalid_guess:

            # ask user for guess
            guess = input("\nguess a word (enter to exit): ")
            guess = guess.lower()
            #print(f'word guessed: {guess}')
    
            if not guess:
                print('Exiting Program')
                exit()
            # check if guess valid
            # check if guess is correct length
            if len(guess) == NWORDLEN:
    
                # check if guess within dictionary
                if guess in DICTION:
                    invalid_guess = False
                    counter += 1
                else:
                    print(f'invalid word. not found in dictionary')
            else:
                print(f'word must be of length {NWORDLEN}')
            

        # add guess to board
        b.update_board(guess, counter)
        
        # display options
        #b.print_choices() 
        
        # display board
        b.print_board()

        # if the guess is the same as target word
        if guess == TARGET:
            print(f'\nYou Win!\nFound target in {counter} guesses')
            correct_guess = True

        # if reached max guesses
        if counter == NGUESSES:
            print(f'\nOut of guesses. The word was {TARGET}')
            break
            

if __name__=="__main__":
    main()
