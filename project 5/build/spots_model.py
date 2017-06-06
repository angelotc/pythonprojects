import point

class Spot:
    def __init__(self, center: point.Point, radius_frac: float):
        self._enter = center
        self._radius_frac = radius_frac

    def center_point(self) -> point.Point:
        return self._center

    def radius_frac(self) -> float:
        return self._radius_frac

    def contains(self, p:point.Point) -> bool:
        return p.distance_from_frac(self._center) 
    
class SpotState:
    def __init__(self):
        self._spots = [         # x     y    radius
            Spot(point.from_frac(0.5, 0.5), 0.05),
            Spot(point.from_frac(0.1, 0.8), 0.1),
            Spot(point.from_frac(0.3, 0.2), 0.02)
                ]
    def all_spots(self) -> [Spot]:
        self._spots

    def handle_click(self, click_point: point.Point) ->None:
        for spot in reversed(self._spots):
            if spot.contains(click_point):
                self._spots.remove(spot)
                return



            self._spots.append(Spot(click_point, _SPOT_RADIUS_FRAC))



    
