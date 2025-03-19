from src.figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise ValueError('Sides must be numbers')
        if radius <=0:
            raise ValueError("A circle with this radius does not exist")
        self.radius = radius


    @property
    def get_area(self):
        return 3.14 * self.radius**2

    @property
    def get_perimetr(self):
        return 2 * 3.14 * self.radius
