import pytest
from src.figure import Figure
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle

@pytest.mark.parametrize('figure_1, figure_2, expected_sum',
                         [(Rectangle(3, 4), Rectangle(1, 4), 16),
                          (Circle(3), Circle(1), 31.4),
                          (Triangle(3, 4, 5), Triangle(4, 4, 7), 12.78),
                          (Square(3), Square(2), 13),
                          (Rectangle(7, 8), Square(4), 72),  # Mixing Rectangle and Square
                          (Circle(10), Square(7), 363),  # Mixing Circle and Square
                          (Triangle(10, 24, 26), Circle(5), 198.5),  # Mixing Triangle and Circle
                          ],
                         ids=['Rectangles', 'Circles', 'Triangles', 'Squares',
                              'Rect_Square', 'Circ_Square', 'Tri_Circ']

)
def test_add_area_valid(figure_1, figure_2, expected_sum):
    assert round(figure_1.add_area(figure_2), 2) == expected_sum, f"Expected sum {expected_sum}"




@pytest.mark.parametrize(
    "not_figure",
    [3, "test", 2.4],
    ids=["integer", "string", "float"]
)
def test_add_area_invalid(not_figure):
    rect = Rectangle(3, 4)
    with pytest.raises(ValueError, match=f"{not_figure} not a Figure object"):
        rect.add_area(not_figure)