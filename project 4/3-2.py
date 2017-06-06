import tkinter

class RingsApplication:
    def __init__(self, rings):
        
        self._rings = rings
        
        self._root_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 400,
            background = 'red')

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        

        self._canvas.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E   )

    
        
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0 , weight = 1)

    
    def run(self)->None:

        self._root_window.mainloop()

    def _on_canvas_resized(self, event: tkinter.Event)->None:
        #delete all the shapes from the canvas

        #self._canvas.delete(tkinter.ALL)
        
        pixel_width = self._canvas.winfo_width()
        pixel_height = self._canvas.winfo_height()
        
        for frac_x1, frac_y1, frac_x2, frac_y2 in self._rings:
            self._canvas.create_oval(
                frac_x1 * pixel_width, frac_y1 * pixel_height,
                frac_x2 * pixel_width, frac_y2 * pixel_height,
                outline = 'yellow')
            
            
              

if __name__ == '__main__':
    c = RingsApplication([
        (0.2, 0.2, 0.3, 0.3),
        (0.45, 0.15, 0.6, 0.7),
        (0.85, 0.3, 0.9, 0.45)
        ])
    run(c)
    
