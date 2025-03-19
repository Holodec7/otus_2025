import pytest

@pytest.fixture()
def rectangle_sides_check():
    def _wrapper(sides:str):
        if sides == 'int':
            return 3, 5
        elif sides == 'float':
            return 2, 1.1
        else:
            raise ValueError
    return _wrapper
