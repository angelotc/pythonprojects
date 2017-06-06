#SIMPLE OTHELLO

class GameState:
    def __init__( self):
        self._white  = 'W'
        self._black = 'B'
        self._empty = '.'
        
        self._turn = None #'B' or 'W'
        self._winner = None
        self._board = ''
        self._rows = 0
        self._cols = 0

    def new_game(self, rows: int, cols: int, turn: 'str')-> None:
        
        board = []

        for i in range(rows):
            board.append([])
            for j in range(cols):
                board[-1].append(self._empty)
            
        board[int(rows/2)-1][int(cols/2)-1] = self._black
        board[int(rows/2)][int((cols/2))] = self._black
        board[int(rows/2)][int((cols/2)-1)] = self._white
        board[int((rows/2)-1)][int(cols/2)] = self._white
        self._board = board
        self._turn = turn
        self._rows = rows
        self._cols = cols

   
    def print_board(self):
        for row in self._board:
            row_str = ''
            for item in row:
                row_str += item+ ' '
            print(row_str[:-1])



    def count_chips(self)->(int, int):
        blacks = 0
        whites = 0
        for row in self._board:
            for col in row:
                if col == self._black:
                    blacks +=1
                elif col == self._white:
                    whites +=1
        return blacks, whites
        print('B: {} W: {}'.format(blacks, whites))
        

    def opposite_exists(self)->bool:
        for row in self._board:
            if self.other_turn in row:
                pass

    def is_valid_move(self, move:list)->bool:
        '''given a 2 item list as input, determines if the move is valid'''
        row = int(move[0])-1
        col = int(move[1])-1
        try:
            if self._board[row][col] != '.':
                print('INVALID')
                return False
            elif self.other_turn() not in self.surrounding_chips(move):
                print('INVALID')
                return False
            else:
                print('VALID')
                return True
        except:
            print('INVALID IE')
            return False

            
    
    def read_board(self)-> list:
        '''preset the board'''
        count = 0
        for row in self._board:
            x = input().split()
            self._board[count] = x
            count +=1
        return self._board

    def switch_turns(self):

        if self._turn == 'W':
            self._turn = 'B'
        elif self._turn == 'B':
            self._turn = 'W'


    def print_turn(self)->None:
        print('TURN: ' + self._turn)

    def surrounding_chips(self, move: list)->list:
        '''checks for surrounding chips using incremnets'''
        increments = [[-1, -1], [-1, 0], [-1, 1],
                      [ 0, -1],          [ 0, 1],
                      [ 1, -1], [ 1, 0], [ 1, 1]]
        surr_chips = []
        row = int(move[0])-1
        col = int(move[0])-1
      
        for item in increments:
            dummy_row = row + item[0]
            dummy_col = col + item[1]
            
            
            
            if (dummy_row <= (self._rows-1) and dummy_row > 0) or (dummy_col <= (self._cols-1) and dummy_col > 0):
                #chip is a 3-element list (row, col, value)
                chip = []
                chip.append(dummy_row)
                chip.append(dummy_col)
                #chip.append(self._board[dummy_row][dummy_col])
                surr_chips.append(chip)
            
        return surr_chips

    
    def other_turn(self)-> str:
        if self._turn == 'W':
            return self._black
        else:
            return self._white
  


#NEEDS WORK
    
    def flip_tiles(self, move:list):
        for item in self.surrounding_chips(move):
            item[2]
        

    def check_winner(self):
        '''checks current gameboard state (relative to winner?) and decides
            if winner exists'''
        if '.' not in self._board:
            return True

    def increment_diagonal(self) -> None:
    # We need only one loop, as opposed to two, because the sequence of
    # indices we want is: x[0][0], x[1][1], x[2][2], etc.  The index in the
    # two dimensions never vary independently in this problem.
    #
    # The "if" statement is there to be sure that the i-th sublist has
    # enough elements in it.

        for i in range(len(self)):
            if i < len(self[i]):
                self[i][i] += 1



    
  
        

if __name__ == '__main__':
    c =GameState()
    c.new_game(4,4,'B')
    c.print_board()
    x = ['4', '4']
    
