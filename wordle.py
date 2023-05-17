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

    # print TARGET word for debugging purpose
    print(f'Goal: {TARGET}')
    
    # list of letters for each color assignment
    lgreen = [[] for x in range(NWORDLEN)]
    lyellow = [[] for x in range(NWORDLEN)]
    lgrey = []

    # initializing trackers for length of game
    correct_guess = False
    counter = 0

    # while remaining guess available or guesses target
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

            for j in range(NWORDLEN):
                #print(f'{target[j]}')
                
                # if letter in correct position and within target
                if i == j and glet is TARGET[j]:
                        #if gletter not in lgreen[i]:
                            
                            # color green
                            lgreen[i].append(glet)

                            # set tile to row = counter, col = i, letter = glet, color = green
                            b.set_tile(counter - 1, i, glet, 'green')
                
                # if letter in target but incorrect position
                if i != j and glet is TARGET[j]:
                    #if gletter not in lyellow[i]:

                        # color yellow
                        lyellow[i].append(glet)

                        # set tile to row = counter, col = i, letter = gletter, color = yellow
                        b.set_tile(counter - 1, i, glet, 'yellow')
                

            # if letter not within word
            if glet not in lgreen[i]:
                if glet not in lyellow[i]:
                    #if glet not in lgrey:

                    # color grey
                    lgrey.append(glet)
        
                    # set tile to row = counter, col = i, letter = gletter, color = grey 
                    b.set_tile(counter - 1, i, glet, 'grey')
                
        print(f'green: {lgreen}\nyellow: {lyellow}\ngrey: {lgrey}')
        
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
