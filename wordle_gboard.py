#!/usr/bin/env python
"""
A Wordle board holds a matrix of tiles.

"""

# Size of Puzzle
from wordle_config import NGUESSES, NWORDLEN 

# Choices is the alphabet, unknown for a tile without a letter is '.'
from wordle_config import CHOICES, UNKNOWN


class Board():

    def __init__(self):
        # number of rows = number of guesses
        # number of cols = number of letters within valid word
        self.board = []
        self.groups = []

        for row in range(NGUESSES):
            cols = []
            for col in range(NWORDLEN):
                cols.append(Tile(row, col))
            self.board.append(cols)



    def print_board(self):
        
        print(f'*** Wordle Game Board ***')
        
        for row in self.board:
            #letters = [tile.letter for tile in row]
            letters = ""
            for tile in row:
                #print(f'{tile.letter}')
                letters = letters + tile.letter

            print(f'{letters}')
            


        """
        for i in range(NGUESSES):
            
            for j in range(NWORDLEN):
                
                print(f'{self.board[i][j].letter}'.strip())
        """ 
        


class Tile:

    def __init__(self, row: int, col: int, letter='.', color='grey'):
        self.row = row
        self.col = col
        self.letter = letter
        self.color = color

    def __str__(self):
        return f'Tile: {self.letter} {self.color}'

    def __repr__(self):
        return f'Tile(letter={self.letter}, color={self.color}, row={self.row}, col={self.col})'


def main():
    # checking if import works
    #print(CHOICES, NGUESSES)

    x = Tile(1, 2, 'f', 'yellow')
    print(x)

    z = Tile(3, 5)
    print(z)
    
    
    y = Board()
    y.print_board()



main()

