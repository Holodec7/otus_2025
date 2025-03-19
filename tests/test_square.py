import pytest
from src.square import Square

@pytest.mark.parametrize(
    "side_a",
    [0, -5, "four"],
    ids=["side_a==0", "Negative", "Non-numeric"]
)
def test_square_exist(side_a):
    with pytest.raises(ValueError):
        Square(side_a)

def test_square_side():
    s = Square(3)
    assert s.side_a == 3, "Stored values should match the expected"


@pytest.mark.parametrize(
    "side_a, area",
    [(3, 9),
     (2.5, 6.25),
     (1, 1),
     (0.01, 0.0001),
     (999999, 999998000001)],
    ids = ["integer", "float", "small_area", "very_small_area", "big_area"]
)
def test_square_area(side_a, area):
    s = Square(side_a)
    assert s.get_area == area, f'Area should be {area}'


@pytest.mark.parametrize(
    "side_a, perimetr",
    [(4, 16),
     (4.5,  18)],
    ids = ["integer", "float"]
)
def test_square_perimetr(side_a, perimetr):
    s = Square(side_a)
    assert s.get_perimetr == perimetr, f'Perimetr should be {perimetr}'