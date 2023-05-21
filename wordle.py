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
    print(f'Goal: {TARGET}')

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
            guess = input("guess a word: ")
            guess = guess.lower()
            print(f'word guessed: {guess}')


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
        
        # find corresponding colors
        for i in range(NWORDLEN):
            #print(f'{guess[i]}')
            glet = guess[i]
            print(f'\nProcessing - {glet} - position: {i}')

            for j in range(NWORDLEN):
                #print(f'{target[j]}')
                print(f'comparing with - {TARGET[j]} - position: {j}')
                
                # if letter in correct position and within target
                if i == j and glet is TARGET[j]:
                    print(f'letter and position match')

                    # color green
                    b.greens[i].append(glet)

                    # Set Tile
                    b.set_tile(counter - 1, i, glet, 'green')
                    
                    # update options
                    b.update_choices(i, glet, 'green')
            
                # if letter in target but incorrect position
                if i != j and glet is TARGET[j]:
                    print(f'letter match, position incorrect')
                    
                    # If glet is in green, already know where the correct position is 
                    if glet not in b.greens[i]:
                        
                        
                        # If already in yellow, no need to update
                        if glet not in b.yellows[i]:
                            
                            # color yellow
                            b.yellows[i].append(glet)
                            
                            # Update options
                            b.update_choices(i, glet, 'yellow')
                        
                        # create Tile for board
                        b.set_tile(counter - 1, i, glet, 'yellow')
                            


            # if letter not within word
            print(f'Checking if grey by default')
            if glet not in b.greens[i]:
                print(f'not within greens in position {i}')
                if glet not in b.yellows[i]:
                    print(f'not within yellows in position {i}')

                    # color grey
                    b.greys.append(glet)
        
                    # set Tile
                    b.set_tile(counter - 1, i, glet, 'grey')
                    
                    # update options
                    b.update_choices(i, glet, 'grey')
                
        # display options
        b.print_choices() 
        
        # display board
        b.print_board()

        # if the guess is the same as target word
        if guess == TARGET:
            print(f'You Win!')
            correct_guess = True

        # if reached max guesses
        if counter == NGUESSES:
            print(f'Out of guesses. The word was {TARGET}')
            break
            


if __name__=="__main__":
    main()
