"""
A Wordle board holds a matrix of tiles.

"""

# Size of Puzzle
from wordle_config import NGUESSES, NWORDLEN 

# Choices is the alphabet, unknown for a tile without a letter is '.'
from wordle_config import CHOICES, UNKNOWN



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

Need to figure out:
    - should above be in a new class, added to class Board, or not a class at all?
    - where should choices for each column be stored

Target word
    - should be random word from text file
    - where should this be stored?
    - how to keep track across files?
"""



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


if __name__=="__main__":
    main()
