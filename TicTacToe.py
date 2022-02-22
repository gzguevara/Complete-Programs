'''
Reversed Tic Tac Toe on a 10x10 field with condition 5 in row looses.
'''

import random
from math import *

#Defines the Humans marker
def players_marker():
    
    ready = ''

    while ready != 'yes':

        print('In my version of the game you can choose the marker you play with.')
        print('You will play against the computer with marker "O".')
        mark = input('Chose one sign as your marker: ')
        print('\n')
        print('We will choose randomly who starts.')
        ready = input('Are you ready? "yes" or "no" ')
        print('\n')

        while ready == 'no':
            ready = input('Ok... Are you ready now? "yes" or "no" ')
            print("\n")
        
        if ready not in ['yes', 'no']:
            print("I don't understand what you typed...")
            print("Let's try again:")
            print("\n")

    return [mark, 'O']

#Sets who starts
def choose_first(markers):

    first_player = markers[random.choice((0, 1))]

    if first_player == markers[0]:
        print(f'Alrigth you will start. Look at the board below and make your choice!')
        print('\n')
    else:
        print(f'Alrigth. The computer starts. Look at the board below and make your choice!')
        print('\n')
    
    return first_player

#Builds 10x10 board
def build_board(): 
    
    return [[str(num) for num in range((10*j)+1, (10*(j+1))+1)] for j in range(10)]

#Creates inicial parameters for a game by calling the 3 previous defined fuctions
def start_new():
    print('\n')
    print("Let's play reversed Tic Tac Toe!")
    markers = players_marker()
    return markers, choose_first(markers), build_board(), False
    #if you wonder why false, check the main while-loop and then the player_choice fuction

#Prints the board
def display_board(board):

    for row in reversed(board):

        row_print = '-  | '

        for num in row:

            if len(num) == 1: num = ' ' + num + ' '
            elif len(num) == 2: num = ' ' + num
            
            row_print += num + ' | '
        
        print('-  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -')
        print(row_print)

    print('-  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -')
    print('\n')

#Returns the correct indicies of a number in the board
def get_position(position):

    line      = ceil(position/10) - 1
    position  = position - 1 - (line) * 10

    return (line,position)

#Sets an entry in the board equal to a marker
def place_marker(board, mark, position):

    line, position_in_line = get_position(position)

    board[line][position_in_line] = mark

    return position

#Checks on a list whether there are 5 of the same markers in a given list
def five_in_line(line, mark):

    best = 0
    cur_count = 0

    for i in range(len(line)):

        if line[i] == mark :
            cur_count +=1    
            best = max(cur_count, best)

        else:
            cur_count = 0

    return best >= 5

#Build lists for all rows and columns and traces AND calls the previous fuction on all of those lists
def lose_check(board, mark):

    # Horizontal and vertical line
    for i in range(10):

        # Construct the vertical line
        vertical = []
        for j in range(10): vertical.append(board[j][i])
        
        # Check the vertical line
        if five_in_line(vertical, mark): return True
        # Check the horizontal line
        if five_in_line(board[i], mark): return True
    
    #Left-right, right-left (all) Traces
    for i in range(6):
        

        ######## Traces right to left ########
        # Get indicies
        row = list(range(0+i,10))
        col = list(range(0,10-i))

        # Construct paralell tarces
        trace_up   = []
        trace_down = []
        for j in range(len(row)):
            
            trace_up.append(board[row[j]][col[j]])
            trace_down.append(board[col[j]][row[j]])
        
        # Check upper and lower trace
        if five_in_line(trace_up, mark): return True
        if five_in_line(trace_down, mark): return True


        ######## Traces left to right ########
        # Get indicies
        row = list(reversed(range(0,10-i)))

        # Construct paralell tarces
        trace_up   = []
        trace_down = []
        for j in range(len(row)):
            
            trace_up.append(board[row[j]][col[j]])
            trace_down.append(board[row[j]+i][col[j]+i])
        
        # Check upper and lower trace
        if five_in_line(trace_up, mark): return True
        if five_in_line(trace_down, mark): return True
    
    return False

#Returns a set of strings of all unique numbers on the board
def unique_elements_board(board):

    return set([inner for outer in board for inner in outer]).difference(PLAYERS_MARKS)

#Verifies the humans choice
def player_choice(board, computer_choice, mark):
    
    position = 0

    while True:

        try:
            #note that computer_choice will mostly be a non-empty string  - therefore "True"
            if computer_choice:
                position = int(input(f'The computer chose "{computer_choice}". Choose your next position from 1 to 100: '))
            
            #computer choice will be only "Fasle" at the beginning of a game
            #if the computer starts the first round
            else: 
                position = int(input(f'Choose your next position from 1 to 100: '))
                
        except ValueError as exc:
            print(f'Wrong value: {exc}. Is not a number!')
            continue

        if str(position) in unique_elements_board(board):

            #if everything is correct it sets the position 
            place_marker(board, mark, position)
            next_round()
            break
            
        else:
            print(str(position) + ' is not in the range from 1 to 100 or it is alrady taken!')

#Computer's Strategy
#The computer pops randomly from a set of free field.
#If the pick would lead to a loss, than it pops the next element in the list
#If this list's length is 1 than it just picks this last element and probably loses
def strategy(board, mark):

    unique_choices = list(unique_elements_board(board))

    while True:
        
        #create copy of board
        check_board   = [line.copy() for line in board]
        #pop one element from the list of free fields
        random_choice = int(unique_choices.pop())
        #place this element in the board
        place_marker(check_board, PLAYERS_MARKS[1], random_choice)
        #Check whether this element leads to a loss or if we do'nt have more elements to try 
        if not lose_check(check_board, PLAYERS_MARKS[1]) or len(unique_choices) == 0: 
            
            return place_marker(board, mark, random_choice)
    
#Asks whether human wants to play again
def replay():

    decision = ''
    while decision not in ('yes', 'no'):
        print('\n')
        decision = input('Would you like to play again? "yes" or "no"').lower()
        print('\n')

    return decision == 'yes'

#Visual switch between the rounds
def next_round():
    print('\n' * 2)
    print('-  |  -  |  -  |  -  |  -  | NEXT ROUND |  -  |  -  |  -  |  -  |  -')
    print('\n' * 2)

#Switches the players marker
def switch_player(curent_player):
    
    return 'O' if curent_player== PLAYERS_MARKS[0] else PLAYERS_MARKS[0]

#Checks whether game came to a finish condition
def check_game_finish(board, mark):
    
    #win
    if lose_check(board, mark):
        print('\n')
        print(f'The player with the mark "{mark}" looses!')
        print('\n')
        return True

    #ничья
    if len(unique_elements_board(board)) == 2:
        print('\n')
        print('The game ended in a draw.')
        print('\n')
        return True

    return False


############################## START OF THE GAME ###############################

PLAYERS_MARKS, CURRENT_PLAYER_MARK, PLAY_BOARD, COMPUTERS_POSITION = start_new()

while True:

    #Humans turn
    if CURRENT_PLAYER_MARK == PLAYERS_MARKS[0]:
        display_board(PLAY_BOARD)
        player_choice(PLAY_BOARD, COMPUTERS_POSITION, CURRENT_PLAYER_MARK)
    
    #Computers turn
    else:
        COMPUTERS_POSITION = strategy(PLAY_BOARD, CURRENT_PLAYER_MARK)
   
    #Check for finishing conditon of the game
    if check_game_finish(PLAY_BOARD, CURRENT_PLAYER_MARK):
        display_board(PLAY_BOARD)

        if replay():
            PLAYERS_MARKS, CURRENT_PLAYER_MARK, PLAY_BOARD, PLAYER_POSITION = start_new()
            continue

        break
    
    #Switch player before next round
    CURRENT_PLAYER_MARK = switch_player(CURRENT_PLAYER_MARK)



