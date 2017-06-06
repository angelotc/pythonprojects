#spots_view.py


import tkinter
import spots_model
import point




class SpotsApplication:
    def __init__(self):
        self._state = spots_model.SpotsState()
        self._root_window = tkinter.Tk()
        

        self._canvas = tkinter.Canvas(
            master = self._root_window , width = 600, height = 500,
            background = 'purple')


        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        self._canvas.bind('<Configure>', self._on_canvas_resized)

        self._canvas.grid(
            row = 0, column = 0, padx = 10, pady = 10, 
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._root_window.rowconfigure( 0, weight = 1)
        self._root_window.columnconfigure( 0, weight = 1)
        
    def run(self) -> None:
        self._root_window.mainloop()

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        print('Clicked @ {}, {}'.format(event.x, event.y))

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._draw_spots()


    def _draw_spots(self) -> None:
        for spots in self._state.all_spots():
            self._draw_spot(spot)

    def _draw_spot(self, spot: spots_model.Spot) -> None:
        self._canvas.delete(tkinter.ALL)
        center_frac_x, center_frac_y = spot.center_point().frac()
        radius_frac = spot.radius_frac()
        topleft_frac_x = center_frac_x - radius_frac
        topleft_frac_x = center_frac_x - radius_frac
        topleft = Point.from_frac(topleft_frac_x, topleft_frac_y)
        
        bottomleft_frac_x = center_frac_x + radius_frac
        bottomleft_frac_x = center_frac_x + radius_frac
        bottomleft = point.from_frac(bottomright_frac_x, bottomright_frac_y)

        topleft_pixel_x, topleft_pixel_y = topleft.pixel(width, height)
        bottomright_pixel_x, bottomright_pixel_y = bottomright.pixel(width, height)

        self._canvas.create_oval(
            topleft_pixel_x, topleft_pixel_y,
            bottomright_pixel_x, bottom_right_pixel_y, fill = 'yellow')
        


if __name__ == '__main__':
    app = SpotsApplication()
    app.run()

    SpotsApplication().run()

    

