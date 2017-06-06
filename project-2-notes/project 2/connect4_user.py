#Angelo Cortez 43373142 and Ruowan Yang 74391124

import connect4
import I32CFSP
from utilities import *



def turn(board: connect4.GameState)-> str:
    '''  used to indicate whose turn it is in the main() function'''
    if board.turn == 1:
        return 'red'
    elif board.turn == 2:
        return 'yellow'



def main():
    currentgame = connect4.new_game()
    print_board(currentgame.board)
    while True:
        
        print('It is color ' + turn(currentgame) + "'s turn.")
        firstinput = str(input ('Drop or pop? (e.g. Type "DROP 5" or "POP 4"): ')).upper()
        try:
            if 'DROP' in firstinput:
                currentgame = connect4.drop(currentgame, int(firstinput[5])-1)
                
                if connect4.winner(currentgame)==1:
                    print_board(currentgame.board)
                    print('Red wins!')
                    break
                
                elif connect4.winner(currentgame) ==2:
                    print_board(currentgame.board)
                    print('Yellow wins!')
                    break
                
                print_board(currentgame.board)

                
            elif 'POP' in firstinput:

                currentgame = connect4.pop(currentgame, int(firstinput[4])-1)
                if connect4.winner(currentgame)== 1:
                    print_board(currentgame.board)
                    print('Red wins!')
                    break
                elif connect4.winner(currentgame) == 2:
                    print_board(currentgame.board)
                    print('Yellow wins!')
                    break
                print_board(currentgame.board)
                
            else:
                print('Error with input.')
        except:
            print('Input error has occured.\n(e.g. Type "DROP 5" or "POP 4")')

if __name__ == '__main__':
    print ( 'Welcome to Connect Four by Angelo and Michelle')    
    main()
    
    
