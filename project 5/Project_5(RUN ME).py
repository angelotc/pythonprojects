import tkinter
import Project_5_logic

#Angelo Cortez 



_DEFAULT_FONT = ('Helvetica', 14)
_ERROR_FONT = ('Helvetica', 12)

class NameDialog:
    def __init__(self):
 
        self._dialog_window = tkinter.Toplevel()
        #LABEL

        who_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Game Setup', font = _DEFAULT_FONT)
        who_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)

        

        #ROWS

        self._row_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Rows:' , font = _DEFAULT_FONT)

        self._row_label.grid(
            row = 1, column = 0, padx = 5, pady = 5)
        
        self._row_entry = tkinter.Entry(
            master = self._dialog_window,
            width = 20, font = _DEFAULT_FONT)

        self._row_entry.grid(
            row = 1, column = 1, padx = 5, pady = 5)

        #COLUMNS

        self._column_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Columns:' , font = _DEFAULT_FONT)

        self._column_label.grid(
            row = 2, column = 0, padx = 5, pady = 5)

        self._column_entry = tkinter.Entry(
            master = self._dialog_window,
            width = 20, font = _DEFAULT_FONT)

        self._column_entry.grid(
            row = 2, column = 1, padx = 5, pady = 5)
        
        #MODES

        self._game_type_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Game Type:', font = _DEFAULT_FONT)

        self._game_type_label.grid(
            row = 3, column = 0, padx = 5, pady = 5)

        self._game_type_entry = tkinter.Entry(
            master = self._dialog_window,
            width = 20, font = _DEFAULT_FONT)

        self._game_type_entry.grid(
            row = 3, column = 1, padx = 5, pady = 5)

        #FIRST
       

        self._goes_first_label = tkinter.Label(
            master = self._dialog_window,
            text = 'First Turn?:', font = _DEFAULT_FONT)

        self._goes_first_label.grid(
            row = 4, column = 0, padx = 5, pady = 5)

        self._goes_first_entry = tkinter.Entry(
            master = self._dialog_window,
            width = 20, font = _DEFAULT_FONT)

        self._goes_first_entry.grid(
            row = 4, column = 1, padx = 5, pady = 5)
        
        
        #GAMETYPE

        #self._game_type = tkinter.Checkbutton(
            #master = self._dialog_window,
            #text = 'Game Type', 

        button_frame = tkinter.Frame(
            master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 1, padx =5, pady = 5)

        ok_button = tkinter.Button(
            master = button_frame,
            text = 'OK', font = _DEFAULT_FONT,
            command = self._on_ok_clicked)

        ok_button.grid(row = 0, column = 0)

        cancel_button = tkinter.Button(
            master = button_frame,
            text = 'Cancel', font = _DEFAULT_FONT,
            command = self._on_cancel_clicked)

        cancel_button.grid(row = 0, column = 1)

        self._set_rows = 0
        self._set_cols = 0
        self._ok_clicked = False
        self._first = ''
        self._game_type = ''


        self._game =  Project_5_logic.GameState()

        

    def show(self) -> None:
##        print('Before')
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()
##        print('aafter')


    def _on_ok_clicked(self) -> None:
        
        self._set_rows = int(self._row_entry.get())
        self._set_cols = int(self._column_entry.get())
        self._first = self._goes_first_entry.get()
        self._game_type = self._game_type_entry.get()
        if self._set_rows %2 != 0 or self._set_cols %2 != 0:
            
            error_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Error. Rows and columns must be even', font = _ERROR_FONT)
            error_label.grid(
            row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
            
        elif self._set_rows < 4 and self._set_rows > 16 or self._set_cols > 16 and self._set_cols < 16:
            
            error_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Error. Rows and columns must be 4 - 16', font = _ERROR_FONT)
            error_label.grid(
            row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)

        elif  self._first not in ['B','W']:
            #print(self._first)
            error_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Error. First turn must be B or W.', font = _ERROR_FONT)
            error_label.grid(
            row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)

        elif  self._game_type not in ['>','<']:
            
            error_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Error. Enter > or < for game type.', font = _ERROR_FONT)
            error_label.grid(
            row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)

        else:
            
            self._ok_clicked = True
            self._game.new_game(self._set_rows, self._set_cols, self._first)
            self._game._turn = self._first
            self._game._game_type = self._game_type

            #print(self._game._turn)
            
            
                                
            
            self._dialog_window.destroy()
            
            
            
        
        

    def _on_cancel_clicked(self) -> None:
        self._dialog_window.destroy()

    def was_ok_clicked(self) -> bool:
        return self._ok_clicked
    
    def get_game(self)->  Project_5_logic.GameState():
        return self._game


    

class Othello:
    def __init__(self):
        
        self._root_window = tkinter.Tk()
        # Preset the GameState to test
        
        self._gamestate =  Project_5_logic.GameState()
        

        
        self._filled = []


        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 600,
            background = 'Cyan')
        self._canvas.pack()
        
        
        self._canvas.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        #GAME BOARD


        
        # Tkinter control variable
        self._greeting_text = tkinter.StringVar()
        self._greeting_text.set('Welcome to Othello(SIMPLE)!')

        self._blacks = tkinter.StringVar()
        self._blacks.set('Blacks: ' + str(self._gamestate.count_chips()[0]))
        
        self._whites = tkinter.StringVar()
        self._whites.set('Whites: ' + str(self._gamestate.count_chips()[1]))

        white_label = tkinter.Label(master = self._root_window,
            textvariable = self._whites , font = _DEFAULT_FONT)

        white_label.grid(
            row = 3, column = 0, padx = 20, pady = 20, sticky = tkinter.E)



        black_label = tkinter.Label(master = self._root_window,
            textvariable = self._blacks , font = _DEFAULT_FONT)

        black_label.grid(
            row = 3, column = 0, padx = 20, pady = 20, sticky = tkinter.W)

        greeting_label = tkinter.Label(
            master = self._root_window,
            textvariable = self._greeting_text , font = _DEFAULT_FONT)

        greeting_label.grid(
            row = 2, column = 0, padx = 20, pady = 20,
            sticky = tkinter.S)
        #Button

        self._greet_button = tkinter.Button(
            master = self._root_window,
            text = 'Click to play', font = _DEFAULT_FONT,
            command = self._on_greet_clicked)

        self._greet_button.grid(row = 1, column = 0, padx = 20, pady = 20,
            sticky = tkinter.S)

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self.create_grid()

        self._settled = False

        self._first = ''
        self._game_type = ''

        

       

    def run(self) -> None:
        self._root_window.mainloop()

    def create_grid(self):
        
        self._canvas.delete(tkinter.ALL)
        self._width = self._canvas.winfo_width()
        self._height = self._canvas.winfo_height()
        



        
       
        for row in range(self._gamestate._rows):
            
            self._canvas.create_line( ((row+1)/self._gamestate._rows)*self._width, 0,
                         ((row+1)/self._gamestate._rows) *self._width, self._height)

        
        for col in range(self._gamestate._cols):
            self._canvas.create_line(0, ((col+1)/self._gamestate._cols )*self._height, 

                          self._width, ((col+1)/self._gamestate._cols )*self._height    )        
            
    
    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self.create_grid()
        self._redraw_spots()


    
    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        
        col = round((event.x /self._width)/(1/self._gamestate._rows) -0.5)
        row = round((event.y/self._height)/ (1/self._gamestate._cols) -0.5)
        #print(row , col)

        #print(event.x, event.y)
        #print(self._gamestate._turn)
        
        if not self._settled:
            if self._gamestate._board[row][col] == '.':
                self._gamestate._board[row][col] = self._gamestate._turn
                self._filled.append([row, col])
        elif self._settled:
            
            if self._gamestate.valid_empty():
                if self._gamestate._board[row][col] == '.' and self._gamestate.is_valid_move([row+1, col+1]):
                    self._gamestate._board[row][col] = self._gamestate._turn
                    self._filled.append([row, col])
                    self._gamestate.flip_tiles([str(row+1), str(col+1)])
                    self._gamestate.switch_turns()
                    self._greeting_text.set('Turn: '+self._gamestate._turn )
                    
                    if self._gamestate.full_board():
                        self._greeting_text.set(self._gamestate.return_winner())
            else:
                self._gamestate.switch_turns()
                self._greeting_text.set('Turn: '+self._gamestate._turn )
                
                
                
            #print(row,col)
        

        self._blacks.set('Blacks: ' + str(self._gamestate.count_chips()[0]))
        self._whites.set('Whites: ' + str(self._gamestate.count_chips()[1]))
        
          

        

        self._redraw_spots()

    def _redraw_spots(self):
        for spot in self._filled:
            canvas_row = spot[1]
            canvas_col = spot[0]
            if self._gamestate._board[spot[0]][spot[1]] == 'B':
                
                self._canvas.create_oval((canvas_row/self._gamestate._rows)*self._width,
                                         (canvas_col/self._gamestate._cols)*self._height,
                                         ((canvas_row+1)/self._gamestate._rows)*self._width,
                                         ((canvas_col+1)/self._gamestate._cols)*self._height,
                                         fill = 'Black')

            elif self._gamestate._board[spot[0]][spot[1]] == 'W':
                
                self._canvas.create_oval((canvas_row/self._gamestate._rows)*self._width,
                                         (canvas_col/self._gamestate._cols)*self._height,
                                         ((canvas_row+1)/self._gamestate._rows)*self._width,
                                         ((canvas_col+1)/self._gamestate._cols)*self._height,
                                         fill = 'White')
                                         
    def _on_start_clicked(self)-> None:
        self._greet_button.destroy()
        self._gamestate._turn = self._first
        self._greeting_text.set('Turn: '+self._gamestate._turn )
        self._settled = True
        #print(self._gamestate._board)


        
    def _on_switch_clicked(self)->None:
        self._gamestate.switch_turns()
        self._greet_button.destroy()
        self._greeting_text.set('Set '+self._gamestate._turn +' Chips!')
        
        self._greet_button = tkinter.Button(
            master = self._root_window,
            text = 'Click to start', font = _DEFAULT_FONT,
            command = self._on_start_clicked)
             
        self._greet_button.grid(row = 1, column = 0, padx = 20, pady = 20,
            sticky = tkinter.S)
    

    def _on_greet_clicked(self)->None:
        #gamestate set
        # A model dialog box pops up. We wait for that modal dialog box to
        # go away. Ask what happened and make changes appropriately
        dialog = NameDialog()
        
        
        dialog.show()

        if dialog.was_ok_clicked():

            
            
            self._gamestate = dialog._game

            self._first = dialog._first
            #print(dialog._first)
            #print(self._gamestate._turn)
            self.create_grid()
            
            
            self._greeting_text.set('Set '+self._gamestate._turn +' Chips!')
            
            self._greet_button.destroy()
            
            self._greet_button = tkinter.Button(
            master = self._root_window,
            text = 'Click to switch', font = _DEFAULT_FONT,
            command = self._on_switch_clicked)
             
            self._greet_button.grid(row = 1, column = 0, padx = 20, pady = 20,
            sticky = tkinter.S)
            
       

        


        
        
        
            
##def main(c: Othello, g: GameState):
##    c._gamestate = g
##    if g._turn == 'B':
##        c._greeting_text.set("Black's turn.")
##    else:
##        c._greeting_text.set("White's turn.")
        

if __name__ == '__main__':

    c = Othello()
    c.run()
    
