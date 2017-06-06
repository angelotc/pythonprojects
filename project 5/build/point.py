#point.py

# >>> import point
# >>> p1 = point.from_frac(0.5,0.6)
# >>> p1
# <point.Point object ....>
# >>> p1.frac()
# (0.5, 0.6)
# >>> p1.pixel()
# >>> p1.pixel(1000, 800)
# (500, 480)
# >>> p2 = point.from_pixel(400, 600, 800, 800)
# >>> p2.frac()
# (0.5, 0.75)
# >>> p2.pixel(2000,2000)
# (1000, 1500)

class Point:
    def __init__(self, frac_x: float, frac_y: float):
        self._frac_x = frac_x
        self._frac_y = frac_y
        
    def frac(self) -> (float, float):
        return (self._frac_x, self._frac_y)

    def pixel(self, pixel_width: float, pixel_height: float) -> (float, float):
        return(self._frac_x * pixel_width, self._frac_y * pixel_height)
    

def from_frac(frac_x: float, frac_y: float) -> Point:
        return Point(frac_x, frac_y)

def from_pixel(pixel_x: float, pixel_y: float, pixel_width: float, pixel_height: float) -> Point:
        return Point(pixel_x / pixel_width, pixel_y / pixel_height)

