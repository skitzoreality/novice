
'''
tic_tac_toe assignment
'''
import random
board=['1','2','3','4','5','6','7','8','9']
def draw_board():
    '''Gameboard'''
    print('\n')
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-+-+-')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-+-+-')
    print(board[6]+'|'+board[7]+'|'+board[8])
def reset_board():
    '''Reset'''
    return ['1','2','3','4','5','6','7','8','9']
def play():
    '''Play the Game'''
    gameplay=True
    #make first player turn random
    turn=random.randint(2,11)
    draw_board()
    while gameplay:
        if turn%2==0:
            x_o=input('\n\n Please enter square number to place your X: ')
            if not valid_entry(x_o):
                continue
            if check_not_occupied(x_o):
                board[int(x_o)-1]='X'
            else:
                continue
            if check_if_win():
                print('\n\n\n X WINS!!!')
                gameplay=False
            if check_if_draw():
                gameplay=False
            turn+=1
            draw_board()
        else:
            x_o=input('\n\n Please enter square number to place your O: ')
            if not valid_entry(x_o):
                continue
            if check_not_occupied(x_o):
                board[int(x_o)-1]='O'
            else:
                continue
            if check_if_win():
                print('\n\n\n O WINS!!!')
                gameplay=False
            if check_if_draw():
                gameplay=False
            turn+=1
            draw_board()
def check_if_win():
    '''Win conditions'''
    if (board[0]==board[1]==board[2] or
         board[3]==board[4]==board[5] or
         board[6]==board[7]==board[8] or
         board[0]==board[4]==board[8] or
         board[2]==board[4]==board[6] or
         board[0]==board[3]==board[6] or
         board[1]==board[4]==board[7] or
         board[2]==board[5]==board[8]):
        return True
    return False
def check_if_draw():
    '''draw conditions'''
    empty_board=['1','2','3','4','5','6','7','8','9']
    for _, empty in enumerate(empty_board):
        if empty in board:
            return False
    print('\n\n\nDraw\n\n\n')
    return True
def check_not_occupied(x_o):
    '''empty square'''
    if board[int(x_o)-1]=='X' or board[int(x_o)-1]=='O':
        print('\n Oops.\n That space is occupied. Please try again.\n')
        return False
    return True
def valid_entry(x_o):
    '''game input check'''
    empty_board=['1','2','3','4','5','6','7','8','9']
    if x_o not in empty_board:
        print('\n Please enter a valid number')
        return False
    return True


TO_PLAY=True
#Start game/round or Exit
while TO_PLAY:
    yesorno=input('\n\n Would you like to play Tic-Tac-Toe?\n Y to Play, N to Exit:\n')
    if yesorno in ('Y','y'):
        board=reset_board()
        play()
    elif yesorno in ('N','n'):
        TO_PLAY=False
    else:
        print('\n Please enter a valid command')
        continue
