"""
simple wordle game
"""

import wordle_gboard as wgb
from wordle_config import NWORDLEN, NGUESSES

def main():
    # test import
    #b = wgb.Board()
    #b.print_board()

    # pick target word
    # randomize? for now just assign
    target = "wants"
    
    lgreen = []
    lyellow = []
    lgrey = []

    correct_guess = False
    counter = 0
    # while remaining guess available or guesses target
    while not correct_guess:
        
        invalid_guess = True
        
        # ask user for guess
        while invalid_guess:
            guess = input("guess a word: ")
            print(type(guess))
            print(f'word guessed: {guess}')

            # check if guess valid
            if len(guess) != NWORDLEN:
                print(f'word must be of length {NWORDLEN}')
            else:
                invalid_guess = False
                counter += 1
            
            # check if guess within dictionary
            

        # add guess to board

        
        # add corresponding colors
        for i in range(NWORDLEN):
            #print(f'{guess[i]}')
            gletter = guess[i]

            for j in range(NWORDLEN):
                #print(f'{target[j]}')
            
                # if letter in correct position and within target
                if i == j and gletter is target[j]:
                        if gletter not in lgreen:
                            
                            # color green
                            lgreen.append(gletter)
                
                # if letter in target but incorrect position
                if i != j and gletter is target[j]:
                    if gletter not in lyellow:

                        # color yellow
                        lyellow.append(gletter)
            
            # if letter not within word
            if gletter not in lgreen:
                if gletter not in lyellow:
                    if gletter not in lgrey:

                        # color grey
                        lgrey.append(gletter)
        
        print(f'green: {lgreen}\nyellow: {lyellow}\ngrey: {lgrey}')
        # print board

        if guess == target:
            print(f'You Win!')
            correct_guess = True

        if counter == 5:
            print(f'Out of guesses. The word was {target}')
            break
            


if __name__=="__main__":
    main()
