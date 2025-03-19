import pytest
from src.circle import Circle


@pytest.mark.parametrize(
    "radius",
    [0, -5, "four"],
    ids=["radius==0", "Negative", "Non-numeric"]
)
def test_circle_exist(radius):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize(
    "radius, area",
    [(3, 28.26),
     (2.5, 19.625),
     (1, 3.14),
     (0.01, 0.0003),
     (999999, 3139993720003.14)],
    ids = ["integer", "float", "small_area", "very_small_area", "big_area"]
)
def test_square_area(radius, area):
    c = Circle(radius)
    assert round(c.get_area, 4) == round(area,4), 'Area should be {area}'


@pytest.mark.parametrize(
    "radius, perimetr",
    [(4, 25.12),
     (4.5, 28.26)],
    ids = ["integer", "float"]
)
def test_square_perimetr(radius, perimetr):
    c = Circle(radius)
    assert c.get_perimetr == perimetr, f'Perimetr should be {perimetr}'