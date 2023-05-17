"""
simple wordle game
"""

import random
import wordle_gboard as wgb
from wordle_config import NWORDLEN, NGUESSES, DICTION

def main():
    # test import
    b = wgb.Board()
    b.print_board()

    # pick target word
    # randomize? for now just assign
    
#    target = random.choice(DICTION)
    target = "attic"
    print(f'Goal: {target}')
    
    lgreen = [[] for x in range(NWORDLEN)]
    lyellow = [[] for x in range(NWORDLEN)]
    lgrey = []

    correct_guess = False
    counter = 0
    # while remaining guess available or guesses target
    while not correct_guess:
        
        invalid_guess = True
        
        # ask user for guess
        while invalid_guess:
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
        
        
        # add corresponding colors
        for i in range(NWORDLEN):
            #print(f'{guess[i]}')
            gletter = guess[i]
            

            for j in range(NWORDLEN):
                #print(f'{target[j]}')
                
                # if letter in correct position and within target
                if i == j and gletter is target[j]:
                        if gletter not in lgreen[i]:
                            
                            # color green
                            lgreen[i].append(gletter)

                            # set tile to row = counter, col = i, letter = gletter, color = green
                            b.set_tile(counter - 1, i, gletter, 'green')
                
                # if letter in target but incorrect position
                if i != j and gletter is target[j]:
                    if gletter not in lyellow[i]:

                        # color yellow
                        lyellow[i].append(gletter)

                        # set tile to row = counter, col = i, letter = gletter, color = green
                        b.set_tile(counter - 1, i, gletter, 'yellow')
                

            # if letter not within word
            if gletter not in lgreen[i]:
                if gletter not in lyellow[i]:
                    if gletter not in lgrey:

                        # color grey
                        lgrey.append(gletter)
        
                        # set tile to row = counter, col = i, letter = gletter, color = green 
                        b.set_tile(counter - 1, i, gletter, 'grey')
                
        print(f'green: {lgreen}\nyellow: {lyellow}\ngrey: {lgrey}')
        #print board
        b.print_board()

        if guess == target:
            print(f'You Win!')
            correct_guess = True

        if counter == 5:
            print(f'Out of guesses. The word was {target}')
            break
            


if __name__=="__main__":
    main()
