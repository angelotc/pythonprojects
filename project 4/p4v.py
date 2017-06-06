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
        self._game_type = None #< or >

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

        


    def flip_tiles(self, move:list):
        if self.other_turn() in self.surrounding_chips(move):
            print('HI')

    def check_win(self):
        '''checks current gameboard state (relative to winner?) and decides
            if winner exists'''
        interesting = []
        for i in range(self._rows):
            for j in range(self._cols):
                
                if self._board[i][j] == '.':
                    xD= []
                    xD.append(i)
                    xD.append(j)
                    interesting.append(xD)
                    
        for item in interesting:
            print(self.surrounding_coordinates(item))
        if interesting == []:
            b,w = self.count_chips()
            if self._game_type == '>': 
                if b > w:
                    print('WINNER: BLACK')
                elif b < w:
                    print('WINNER: WHITE')
                else:
                    print("WINNER: NONE")
            elif self._game_type == '<':
                if b < w:
                    print('WINNER: BLACK')
                elif b > w:
                    print('WINNER: WHITE')
                else:
                    print("WINNER: NONE")

            
        

    #def check_empty
    
    def is_valid_move(self, move:list)->bool:
        '''given a 2 item list as input, determines if the move is valid'''
        row = int(move[0])-1
        col = int(move[1])-1
        try:
            if self._board[row][col] != '.':
                print('invalid')
                return False
                if self.other_turn() not in self.surrounding_chips(move):
                    print('INVALID')
                    return False
            else:
                print('VALID')
                return True
        except:
            print('INVALID IE')
            return False

    def less_or_more(self)->str:
        xD = input('< or >: ')
        if xD == '<':
            self._game_type = '<'
        else:
            self._game_type = '>'
            
    
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
        col = int(move[1])-1
      
        for item in increments:
            dummy_row = row + item[0]
            dummy_col = col + item[1]
            
              
            if (dummy_row <= (self._rows-1) and dummy_row >= 0) and (dummy_col <= (self._cols-1) and dummy_col >= 0):
                surr_chips.append(self._board[dummy_row][dummy_col])
        
            
        return surr_chips

    def surrounding_coordinates(self, move: list)->[[int,int]]:
        '''checks for surrounding chips using incremnets'''
        increments = [[-1, -1], [-1, 0], [-1, 1],
                      [ 0, -1],          [ 0, 1],
                      [ 1, -1], [ 1, 0], [ 1, 1]]
        surr_coordinates = []
        row = int(move[0])-1
        col = int(move[1])-1
      
        for item in increments:
            dummy_row = row + item[0]
            dummy_col = col + item[1]
               
            if (dummy_row <= (self._rows-1) and dummy_row >= 0) and (dummy_col <= (self._cols-1) and dummy_col >= 0):
                xD = []
                xD.append(dummy_row)
                xD.append(dummy_col)
                surr_coordinates.append(xD)
          
            
        return surr_coordinates

    def other_turn(self):
        if self._turn == 'W':
            return self._black
        else:
            return self._white
        
    def flip_tiles(self, move:list):
        
        surroundedby = self.surrounding_coordinates(move)
        #list surrounding coordinates

        for item in surroundedby:
            if self._board[item[0]][item[1]] == self.other_turn():
                self._board[item[0]][item[1]] = self._turn
        
    def no_valid(self, move:list):
        for row in self._board:
            if '.' in row:
                pass

    def check_winner(self):
        '''checks current gameboard state (relative to winner?) and decides
            if winner exists'''
        for row in self._board:
            if '.' not in row:
                return True

    
         
##    W W W W
##    W W W W 
##    W W W W 
##    W W W . 


if __name__ == '__main__':
    c =GameState()
    c.new_game(4,4,'B')
    c._board =[['W','W','W','W'],['W','W','W','W'],['W','W','W','W'],['W','W','W','.']]
    c.print_board()
    c._turn = 'W'
    x = ['4', '4']
    d = ['4', '3']
    
