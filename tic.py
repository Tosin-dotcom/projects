# tic tac toe X and 0

import random
import time

print("Welcome to a game of Tic Tac Toe")
name = input("Enter your name: ")
print(f"Nice to meet you, {name.title()}")

theBoard = {'top-l': '1', 'top-m': '2', 'top-r': '3',
            'mid-l': '4', 'mid-m': '5', 'mid-r': '6',
            'low-l': '7', 'low-m': '8', 'low-r': '9'}

theBoard2 = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'low-l': ' ', 'low-m': ' ', 'low-r': ' '}


def printBoard(board):
    print(f"{board['top-l']}  | {board['top-m']} | {board['top-r']}")
    print('---+---+---')
    print(f"{board['mid-l']}  | {board['mid-m']} | {board['mid-r']}")
    print('---+---+---')
    print(f"{board['low-l']}  | {board['low-m']} | {board['low-r']}")

  
def verWin(board):
    if (board['top-l'] == board['top-m'] == board['top-r'] or board['mid-l'] == board['mid-m'] == board['mid-r'] or board['low-l'] == board['low-m'] == board['low-r']):
        return True
    
def horiWin(board):
    if board['top-l'] == board['mid-l'] == board['low-l'] or board['top-m'] == board['mid-m'] == board['low-m'] or board['top-r'] == board['mid-r'] == board['low-r']:
        return True
    
def diaWin(board):
    if board['top-l'] == board['mid-m'] == board['low-r'] or board['top-r'] == board['mid-m'] == board['low-l']:
        return True

def win(board):
    if verWin(board) or horiWin(board) or diaWin(board):
        return True        


printBoard(theBoard)

player = input("Choose 'X' or 'O': ").upper()


if player == 'X':
    computer = 'O'
elif player == 'O':
    computer = 'X'

printBoard(theBoard)
print("")
print("")

turn = random.choice([player, computer])
if turn == computer:
    print('Computer plays first')
else:
    print('Player plays first')



a_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(9):
    if turn == computer:
        time.sleep(1)
        move = random.choice(a_choice)
        print(f'Computer picks {move}')
    else:
        move = input('Turn for player. Move to which space?: ')
        
        
    val_list = list(theBoard.values())
    key_list = list(theBoard.keys())
    key = val_list.index(move)
    theBoard[key_list[key]] = turn
    theBoard2[key_list[key]] = turn
    a_choice.remove(move)

    printBoard(theBoard2)
    
    if turn == computer:
        turn = player
        if win(theBoard) == True:
            print("Computer wins!!")
            break
    else:
        turn = computer
        if win(theBoard) == True:
            print("You win!!")
            break
            
    if i == 8:
        print("It is a draw")
