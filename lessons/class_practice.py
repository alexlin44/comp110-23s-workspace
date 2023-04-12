from __future__ import annotations

class Point:
    "Model a 2D Point"

    x: float
    y: float

    def __init__(self, x: float, y:float):
        "Initialize a point with its x,y components"
        self.x = x
        self.y = y

    def scale_by(self, factor: float):
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point: 
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    