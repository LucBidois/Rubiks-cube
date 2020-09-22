from typing import Tuple

from Config import COLS, N, ROWS
from Shapes.Square import Square


class Face:

    def __init__(self, name: str, color: Tuple[float, float, float]):
        self.squares = [Square(i, j, color) for i in range(ROWS) for j in range(COLS)]
        self.name = name

    def __str__(self):
        return self.name

    def colors(self) -> Tuple[Tuple[float, float, float]]:
        """
        returns a tuple of colors to use before
        as the 'before' movement when changing colors
        """
        return tuple(self.squares[i].color for i in range(N ** 2))

    def GLDraw_Face(self, orientation) -> None:
        for square in self.squares:
            square.GLDraw_Square(orientation)
