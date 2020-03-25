def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

import random
def choose_first():
    if random.randint(1,2) == 1:
        print('Player 1 goes first.')
        return ('1', '2')
    else:
        print('Player 2 goes first.')
        return ('2', '1')

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')           #tuple with first and second player marker
    else:
        return ('O', 'X')

def full_board_check(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True


def win_check(board, mark):
    if (board[1] == board[2] == board[3] == mark or
        board[4] == board[5] == board[6] == mark or
        board[7] == board[8] == board[9] == mark or
        board[1] == board[4] == board[7] == mark or
        board[2] == board[5] == board[8] == mark or
        board[3] == board[6] == board[9] == mark or
        board[1] == board[5] == board[9] == mark or
        board[3] == board[5] == board[7] == mark):
        return True
    return False

def space_check(board, position):
    return board[position] == ' '


def player_choice(board):
    position = ' '
    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or not space_check(board, int(position)):
        position = input('Choose your next position: (1-9) ')

    return int(position)


def place_marker(board, marker, position):
    board[position] = marker


def replay():
    playagain = ''
    while playagain not in ['YES', 'NO', 'Y', 'N']:
        playagain = input("Do you want to play again: Yes or No? ").upper()
    return playagain == 'YES' or playagain == 'Y'



print('Welcome to Tic Tac Toe!')
while True:                                                     #while the game is being re-played
    print('\n' * 100)
    board = [' ']*10
    ex_board = [' ','1','2','3','4','5','6','7','8','9']
    first_player = choose_first()                               #stores value for which player is going first
    mark_result = player_input()                                #stores value for which mark the first player chose
    display_board(ex_board)                                     #shows an example board to the players

    game_on = True
    while game_on:                                              #while this particular game is still going
        for mark in mark_result:                                # 'O' and 'X', in either order
            position = player_choice(board)
            place_marker(board, mark, position)
            display_board(board)
            if win_check(board, mark):
                print('Player ' + first_player[mark_result.index(mark)] + ' won!')     #if this particular mark won, the same index
                                                                                       #of this mark is used to find the player number
                game_on = False                                #to end this particular game
                break                                          #needed to stop the game continuing to the next 'marker' and then stopping
            elif full_board_check(board):
                print('It is a tie!')
                game_on = False
                break
    if not replay():
        print('Thanks for playing!')
        break