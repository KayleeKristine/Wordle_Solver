"""
A Wordle board holds a matrix of tiles.

"""

import random

# Size of Puzzle and Target word
from wordle_config import NGUESSES, NWORDLEN, TARGET 

# Choices is the alphabet, Diction is a list of valid words
from wordle_config import CHOICES, DICTION



"""
Keep track of choices for each col and eliminate
while taking in guesses

Need to keep track of
    if letter not in word (grey)
        - remove letter from choices for each col
    if letter in word but wrong position (yellow)
        - remove letter from choices within current col
    if letter in word and current position (green)
        - Choices for current col = letter
"""



class Board():

    def __init__(self):
        # number of rows = number of guesses
        # number of cols = number of letters within valid word
        self.tiles = []
        self.choices = [CHOICES for i in range(NWORDLEN)]
        
        self.yellows = [[] for i in range(NWORDLEN)]
        self.greens = [[] for i in range(NWORDLEN)]
        self.greys = []

        for row in range(NGUESSES):
            cols = []
            for col in range(NWORDLEN):
                cols.append(Tile(row, col))
            self.tiles.append(cols)


    def print_board(self):
        
        print(f'\n*** Wordle Game Board ***')
        
        for row in self.tiles:
            #letters = [tile.letter for tile in row]
            values = ""
            for tile in row:
                #print(f'{tile.letter}')
                values = values + tile.letter.upper().ljust(1, ' ') + ': ' + tile.color.ljust(8, ' ')

            print(f'{values}')

        self.print_colors()


    def set_tile(self, row_num, col_num, letter, color):
        # fill row with letters from inputed word in indicated row number
        
        tile = self.tiles[row_num][col_num]
        tile.set_value(letter, color)


    def print_choices(self):
        """ Displays possible choices for letters of each position of word """

        print("\n*** Possible Letters for Each Position ***")
        for i in range(NWORDLEN):
            print(f'{i+1} : {self.choices[i]}')


    def print_colors(self):
        """ Displays color lists """

        print("\n*** Green Letters ***")
        print(self.greens)
        
        print("\n*** Yellow Letters ***")
        print(self.yellows)
        
        
        print("\n*** Grey Letters ***")
        print(self.greys)


    def update_choices(self, pos, letter, color):
        """ Eliminates characters from possible letters for each position in word """

        updated_choices = ''
        up_letter = letter.upper()
        #print(f'letter in question: {up_letter}')
        
        # letter in word but wrong position
        # remove choice for current position
        if color == 'yellow':
            #print(f'color is yellow')

            #print(f'previous options: {self.choices[pos]}')
            if up_letter in self.choices[pos]:
                #print(f'{letter.upper()} is within choices')

                updated_choices = self.choices[pos].replace(up_letter, '-')
                
                self.choices[pos] = updated_choices
                #print(f'updated choices to: {self.choices[pos]} ')
        
        # letter in word and correct position
        # only choice is the letter
        elif color == 'green':
      
            #print(f'color is green')

            #print(f'previous options: {self.choices[pos]}')
            self.choices[pos] = up_letter

            #print(f'updated choices to: {self.choices[pos]} ')

        
        # letter no within word
        # remove choice from all positions
        elif color == 'grey':
           
            #print(f'color is grey')

            #print(f'previous options:')
            #self.print_choices()

            for i in range(NWORDLEN):
                if up_letter in self.choices[i]:
                    updated_choices = self.choices[i].replace(up_letter, '-')
                    self.choices[i] = updated_choices

            #print(f'updated options:')
            #self.print_choices()
        

    
    def update_board(self, guess, counter):
        """ Processes inputted guess word by determining color of tile and placing on board"""

        # find corresponding colors
        for i in range(NWORDLEN):
            #print(f'{guess[i]}')
            glet = guess[i]
            #print(f'\nProcessing - {glet} - position: {i}')

            for j in range(NWORDLEN):
                #print(f'{target[j]}')
                #print(f'comparing with - {TARGET[j]} - position: {j}')
                
                # if letter in correct position and within target
                if i == j and glet is TARGET[j]:
                    #print(f'letter and position match')

                    # add to list of green letters
                    if glet not in self.greens[i]:
                        self.greens[i].append(glet)

                    # Set Tile
                    self.set_tile(counter - 1, i, glet, 'green')
                    
                    # update options
                    self.update_choices(i, glet, 'green')
            
                # if letter in target but incorrect position
                if i != j and glet is TARGET[j]:
                    #print(f'letter match, position incorrect')
                    
                    # If glet is in green, already know where the correct position is 
                    if glet not in self.greens[i]:
                        
                        # If already in yellow, no need to update
                        if glet not in self.yellows[i]:
                            
                            # add to list of yellow letters
                            self.yellows[i].append(glet)
                            
                            # Update options
                            self.update_choices(i, glet, 'yellow')
                        
                        # create Tile for board
                        self.set_tile(counter - 1, i, glet, 'yellow')
                            


            # if letter not within word
            #print(f'Checking if grey by default')
            if glet not in self.greens[i]:
                #print(f'not within greens in position {i}')
                if glet not in self.yellows[i]:
                    #print(f'not within yellows in position {i}')

                    # add to list of grey letters
                    if glet not in self.greys:
                        self.greys.append(glet)
        
                    # set Tile
                    self.set_tile(counter - 1, i, glet, 'grey')
                    
                    # update options
                    self.update_choices(i, glet, 'grey')

        # Display board and updated choices
        self.print_board() 
        self.print_choices()


    def update_cpdict(self, cp_dict):
        """ Eliminates words from possible answers """

        #print(f'{self.greys}')
        
        dict_length = len(cp_dict)
        #print(f'length of cp_dict = {dict_length}')
        
        for i in range(dict_length):
            word = cp_dict[i]
            
            if len(word) != 0:

                # if word contains a grey letter, discard
                if any([x in word for x in self.greys]):
                    cp_dict[i] = ''
                
                for j in range(NWORDLEN):

                    # if word contains yellow letter in corresponding position, discard
                    if any([x in word[j] for x in self.yellows[j]]):
                        
                        if not any([x in word[j] for x in self.greens[j]]):
                            cp_dict[i] = ''
                
                    # if word does not contain green letter in corresponding position, discard
                    if any([x not in word[j] for x in self.greens[j]]):
                        cp_dict[i] = ''
        
        new_cpdict = []
        for i in range(dict_length):    
            if len(cp_dict[i]) != 0:
                new_cpdict.append(cp_dict[i])
                
        #print(new_cpdict)
        #print(f'length of update dictionary = {len(new_cpdict)}')
        return new_cpdict


    def solve(self):
        """ solves the wordle through process of elimination """
        # copy dictionary
        cp_dict = DICTION

        # initialize trackers for length of games
        correct_guess = False
        counter = 0

        while not correct_guess:

            invalid_guess = True

            while invalid_guess:
                # choose word
                word = random.choice(cp_dict)
                
                if len(word) == NWORDLEN:
                    if word in DICTION:
                        counter += 1
                        invalid_guess = False
            
            print(f'\nguess a word: {word}')

            # add word to board
            self.update_board(word, counter)

            # narrow down choices within copy of dictionary
            cp_dict = self.update_cpdict(cp_dict)
           

            # repeat until guessed or reached max guesses
            if word == TARGET:
                print(f'\nYou Win!\nFound target in {counter} guess')
                correct_guess = True

            elif counter == NGUESSES:
                print(f'\nOut of guesses. The word was {TARGET}')
                break



class Tile:

    def __init__(self, row: int, col: int, letter='', color=''):
        self.row = row
        self.col = col
        self.letter = letter
        self.color = color

    def set_value(self, l='' , c=''):
        self.color = c
        self.letter = l

    def __str__(self):
        return f'Tile: {self.letter} {self.color}'

    def __repr__(self):
        return f'Tile(letter={self.letter}, color={self.color}, row={self.row}, col={self.col})'


