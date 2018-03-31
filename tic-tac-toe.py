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

def whoGoesFirst():
    # Randomly choose the player who goes firsr.
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # this function returns True if the player wants to play again, otherwise it returns false.
    print('Do you want to play again?(yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter,move):
    board[move] = letter

def isWinner(bo,le):
    # Given a board and a player's letter , this function returns True if that player has won.
    #bo=board, le=letter

    return ((bo[7]==le and bo[8]== le and bo==[9]==le)or #across the top
    (bo[4] == le and bo[5] == le and bo == [6] == le) or  #across the middle)
    (bo[1] == le and bo[2] == le and bo == [3] == le) or  #across the bottom)
    (bo[7] == le and bo[4] == le and bo == [1] == le) or  #down the left side)
    (bo[8] == le and bo[5] == le and bo == [2] == le) or  #down the middle)
    (bo[9] == le and bo[6] == le and bo == [3] == le) or  #down the right side)
    (bo[7] == le and bo[5] == le and bo == [3] == le) or  #diagnol)
    (bo[9] == le and bo[5] == le and bo == [1] == le) )or  #diagnol)








