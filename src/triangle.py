from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if (not isinstance(side_a, (int, float)) or not isinstance(side_b, (int, float)) or not isinstance(side_c, (int, float))):
            raise ValueError("Rectangle sides should be numbers")
        if not (side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_a + side_b):
            raise ValueError("You can not form a valid triangle from the given sides")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("All sides must be positive")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    @property
    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c

