from figure import Figure

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
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

