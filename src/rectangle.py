
from src.figure import Figure

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if not isinstance(side_a, (int, float)) or not isinstance(side_b, (int, float)):
            raise ValueError("Rectangle sides should be numbers")
        if side_a <= 0 or side_b <=0:
            raise ValueError("A rectangle with sides less than and equal to zero does not exist")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimetr(self):
        return 2 * (self.side_a + self.side_b)

