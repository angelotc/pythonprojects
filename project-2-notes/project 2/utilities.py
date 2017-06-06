#Angelo Cortez 43373142 and Ruowan Yang 74391124

import connect4

def print_board(board:connect4.GameState):
    ''' transposes the connect four board into a printable state'''
    
    print( '1 2 3 4 5 6 7')
    
    for i in range(connect4.BOARD_ROWS):
        row_str = ''
        
        for j in range(connect4.BOARD_COLUMNS):
            
            if board[j][i] == 1:
                row_str += 'R '
            elif board[j][i] == 2:
                row_str += 'Y '
            elif board[j][i] == 0:
                row_str += '. '
                
        print(row_str[:-1] )


