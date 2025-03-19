from src.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_a):
        if not isinstance(side_a, (int, float)):
            raise ValueError("Invalid square sides")
        if side_a <= 0:
            raise ValueError("A square with sides less than and equal to zero does not exist")
        super().__init__(side_a, side_a)




