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
        self.tiles = []
        #self.groups = []
        self.choices = [CHOICES for i in range(NWORDLEN)]
        self.yellows = []

        for row in range(NGUESSES):
            cols = []
            for col in range(NWORDLEN):
                cols.append(Tile(row, col))
            self.tiles.append(cols)


    def print_board(self):
        
        print(f'*** Wordle Game Board ***')
        
        for row in self.tiles:
            #letters = [tile.letter for tile in row]
            values = ""
            for tile in row:
                #print(f'{tile.letter}')
                values = values + tile.letter.upper() + ': ' + tile.color + ' '

            print(f'{values}')

    def set_tile(self, row_num, col_num, letter, color):
        # fill row with letters from inputed word in indicated row number
        
        tile = self.tiles[row_num][col_num]
        tile.set_value(letter, color)


    def print_choices(self):
        # print out possible choices for letters of each position of word
        for i in range(NWORDLEN):
            print(self.choices[i])

        print(self.yellows)

    def update_choices(self, pos, letter, color):

        print(f'Entering update_choices()')
        
        updated_choices = ''
        up_letter = letter.upper()
        print(f'letter in question: {up_letter}')
        
        # letter in word but wrong position
        # remove choice for current position
        if color == 'yellow':
            print(f'color is yellow')

            print(f'previous options: {self.choices[pos]}')
            if up_letter in self.choices[pos]:
                print(f'{letter.upper()} is within choices')

                updated_choices = self.choices[pos].replace(up_letter, '-')
                
                self.choices[pos] = updated_choices
                print(f'updated choices to: {self.choices[pos]} ')
        
        # letter in word and correct position
        # only choice is the letter
        elif color == 'green':
      
            print(f'color is green')

            print(f'previous options: {self.choices[pos]}')
            self.choices[pos] = up_letter

            print(f'updated choices to: {self.choices[pos]} ')

        
        # letter no within word
        # remove choice from all positions
        elif color == 'grey':
           
            print(f'color is grey')

            print(f'previous options:')
            self.print_choices()

            for i in range(NWORDLEN):
                if up_letter in self.choices[i]:
                    updated_choices = self.choices[i].replace(up_letter, '-')
                    self.choices[i] = updated_choices

            print(f'updated options:')
            self.print_choices()
        
        print(f'Exiting update_choices()')

class Tile:

    def __init__(self, row: int, col: int, letter='.', color='grey'):
        self.row = row
        self.col = col
        self.letter = letter
        self.color = color

    def set_value(self, l='.' , c='grey'):
        self.color = c
        self.letter = l

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
