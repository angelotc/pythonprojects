import tkinter

##canvas = tkinter.Canvas(master = window, width = 600, height = 500, background = 'purple')
##canvas.pack()
##canvas.create_line(150,125, 540, 250, fill = 'black')
##
##canvas.create_rectangle(200, 200, 300, 300, outline = 'white', fill = 'yellow')




class ScribbleApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()

        self._scribble_canvas = tkinter.Canvas(
            master = self._root_window, width = 700, height = 600,
            background = '#BDEEFF')

        self._scribble_canvas.bind('<Button-1>', self._on_button_down)
        self._scribble_canvas.bind('<ButtonRelease-1>', self._on_button_moved)
        self._scribble_canvas.bind('<Motion>', self._on_button_moved)
        

        self._scribble_canvas.pack()



    def run(self) -> None:
        self._root_window.mainloop()

    def _on_button_down(self, event:tkinter.Event) -> None:
        self._button_is_down = True
        self._last_x = 0
        self._last_y = 0

    def _on_button_up(self, event:tkinter.Event) -> None:
        self._button_is_down = False

    def _on_button_moved(self, event:tkinter.Event) -> None:
        if self._button_is_down:
            self._scribble_canvas.create_line(
                self._last_x, self._last_y, event.x, event.y, 
                fill = 'purple')
            
        self._last_x = event.x
        self._last_y = event.y


if __name__ == '__main__':
    app = ScribbleApplication()
    app.run()

