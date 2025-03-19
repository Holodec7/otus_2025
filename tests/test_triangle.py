import pytest
from src.triangle import Triangle

def test_triangle_side():
    t = Triangle(3, 4, 6)
    assert t.side_a == 3 and t.side_b == 4 and t.side_c == 6, "Stored values should match the expected"
@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [(1, 1, 3),
     (1, 3, 1),
     (3, 1, 1)],
    ids=["side_a + side_b <= side_c", "side_a + side_c <= side_b", "side_b + side_c <= side_a"]
)
def test_triangle_exist(side_a, side_b, side_c):
    with pytest.raises(ValueError, match="You can not form a valid triangle from the given sides"):
        Triangle(side_a, side_b, side_c)

@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [(0, 0, 0), (2.5, 0, 3), (0, 0, 4), (3, 4, 0),
     (-4, -5, -3), (-3, 4, 5), (3, -4, 5), (3, 4, -5),
     ("four", "four", "four"), (8, "four", 6), ("four", 4, 5), (4, 4, "four")],
    ids=["side_a==0", "side_b==0", "side_a==0 side_b==0", "side_c==0",
         "Negative sides", "Negative side_a", "Negative side_b","Negative side_c",
         "Non-numeric sides", "Non-numeric side_b", "a, c non-numeric", "side_c non-numeric"]
)
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(
    "side_a, side_b, side_c, area, perimetr",
    [(3, 4, 5, 6, 12),
     (6, 8, 10, 24, 24),
     (1, 1, 1, 0.4330127018922193, 3),
     (2.5, 6.5, 7.5, 7.890609529687805, 16.5),
     (0.01, 0.01, 0.01, 4.330127018922192e-05, 0.03),
     (1000000, 1000000, 1000000, 433012701892.2193, 3000000)],
    ids=["right_triangle", "scaled_right_triangle", "small_triangle",
         "irregular_triangle", "very_small_triangle", "big_triangle"]
)
def test_triangle_area_and_perimetr(side_a, side_b, side_c, area, perimetr):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area == area, f'Area should be {area}'
    assert t.get_perimetr == perimetr, f'Perimeter should be {perimetr}'

