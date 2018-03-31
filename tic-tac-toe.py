# Tic Tac Toe

import random

def drawBoard(board):
    # This function prints out the board thet it was passed.

    # 'board' is a list of 10 strings representing the board.

    print('    |    |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('    |    |')
    print('------------')
    print('    |    |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('    |    |')
    print('------------')
    print('    |    |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('    |    |')

def inputPlayerLetter():
    # Let the player type which letter they want to be.
    # Return a list with the player's letter as the first item, and the computer's letter as the second.
    letter =''
    while not (letter =='X' or letter=='O'):
        print('Do you want to be X or 0')
        letter = input().upper()

    if letter == 'X':
        return['X','0']
    else:
        return['0','X']

