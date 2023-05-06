#!/usr/bin/env python
"""
A Wordle board holds a matrix of tiles.

"""
"""
class Board():

    def __init__(self, r_num, c_num):
        # number of rows = number of guesses
        # number of cols = number of letters within valid word

        self.board = [[] for i in range(r_num)]
        self.word_size = c_num
        self.total_guesses = r_num

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
        return f'Tile(letter={self.letter}, color={self.color}, row={self.row}, col={self.com})'


def main():
    x = Tile(1, 2, 'f', 'yellow')
    print(x)

main()

