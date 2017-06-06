
from p4 import *

#Angelo Cortez 43373142

def rowcol_input()-> int:
    while True:
        x = int(input())
        if x % 2 != 0:
            print('has to be even')
            continue
        elif (x<4):
            continue
        elif (x>16):
            continue
        else:
            return x

def firstmove()->str:
    while True:
        first_move = input('Who goes first? ("W" or "B"): ')

        if first_move not in  ['B','W']:
            continue
        else:
            return first_move
            break



def main()-> None:
    print('SIMPLE')
    rows = rowcol_input()
    cols = rowcol_input()
    turn = firstmove()
    gamestate = GameState()
    gamestate.new_game(rows, cols, turn)
    gamestate.less_or_more()
    gamestate.read_board()
    while True:
        print('B: {} W: {}'.format(gamestate.count_chips()[0], gamestate.count_chips()[1]))
        gamestate.print_board()
        gamestate.print_turn()
        move = input('MOVE:')
        if move == '':
            gamestate.switch_turns()
            continue
        else:
            pass
        movesplit = move.split()
        print(type(movesplit[0]))
        row = int(movesplit[0])-1
        col = int(movesplit[1])-1
        if len(movesplit)!= 2:
            continue
        elif gamestate.is_valid_move(movesplit):
            if gamestate.other_turn() in gamestate.surrounding_chips(movesplit):
                gamestate._board[row][col] = gamestate._turn
                gamestate.flip_tiles(movesplit)

                gamestate.switch_turns()
                


        elif not gamestate.is_valid_move(movesplit):
            if gamestate.valid_slots():
                gamestate.switch_turns()
        elif gamestate.full_board():
            gamestate.print_board()
            gamestate.print_winner()
            break
            

    

if __name__ == '__main__':
    
    main()
