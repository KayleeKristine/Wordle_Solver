#!/usr/bin/env python
"""
A Wordle board holds a matrix of tiles.

"""

# Size of Puzzle
from wordle_config import NGUESSES, NWORDLEN 

# Choices is the alphabet, unknown for a tile without a letter is '.'
from wordle_config import CHOICES, UNKNOWN


class Board():

    def __init__(self, r_num, c_num):
        # number of rows = number of guesses
        # number of cols = number of letters within valid word

        self.word_size = c_num
        self.total_guesses = r_num
        self.board = [[] for i in range(r_num)]

        for row in range(self.total_guesses):
            cols = []
            for col in range(self.word_size):
                cols.append(Tile(row, col))
            self.board.append(col)
        
    def print_board(self):
        
        f'Wordle Game Board\n'
        for i in range(self.total_guesses):
            f'{i}'
            for j in range(self.word_size):
                f'{j}'
                f'{self.board[i][j]}'
            f'\n'
        


class Tile:

    def __init__(self, row: int, col: int, letter='.', color='grey'):
        self.row = row
        self.col = col
        self.letter = letter
        self.color = color

    def __str__(self):
        return f'Tile: {self.letter}, {self.color}'

    def __repr__(self):
        return f'Tile(letter={self.letter}, color={self.color}, row={self.row}, col={self.com})'


def main():
    # checking if import works
    print(CHOICES, NGUESSES)

    x = Tile(1, 2, 'f', 'yellow')
    print(x)
    

    y = Board(3, 4)
    y.print_board()



main()

