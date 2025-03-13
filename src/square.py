from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("A square with sides less than and equal to zero does not exist")
        super().__init__(side_a, side_a)




