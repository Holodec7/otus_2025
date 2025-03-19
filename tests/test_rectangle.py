from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    "side_a, side_b",
    [(3, 0), (2.5, 0), (0, 0),
     (-4, -5), (-3, 1), (3, -8),
     ("four", 7), (8, "four"), ("four", "five")],
    ids=["side_a==0", "side_b==0", "side_a==0 side_b==0",
         "negative sides", "negative side_a", "negative side_b",
         "non-numeric side_a", "non-numeric side_b", "Both non-numeric"]
)
def test_rectangle_exist(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize('sides', ["int", "float"])
def test_reclangle_sides(rectangle_sides_check,sides):
    side_a, side_b = rectangle_sides_check(sides)
    r = Rectangle(side_a, side_b)
    assert r.side_a == side_a and r.side_b == side_b, "Stored values should match the expected ones"


@pytest.mark.parametrize("side_a, side_b, area",
                         [(3, 5, 15),
                          (2.5, 6.5, 16.25),
                          (1, 1, 1),
                          (0.01, 0.01, 0.0001),
                          (999999, 999999, 999998000001)],
                         ids=["integer", "float", "small_area", "very_small_area", "big_area"]
                         )
def test_rectangle_area(side_a,side_b,area):
    r = Rectangle(side_a, side_b)
    assert r.get_area == area, f'Area should be {area}'


@pytest.mark.parametrize(
    "side_a, side_b, perimetr",
    [(4, 5, 18),
     (4.5, 5.5, 20)],
    ids = ["integer", "float"]
)
def test_rectangle_perimetr(side_a,side_b,perimetr):
    r = Rectangle(side_a, side_b)
    assert r.get_perimetr == perimetr, f'Perimetr should be {perimetr}'
