from Config import COLS, N, ROWS
from Shapes.Square import Square


class Face:

    def __init__(self, name, color):
        self.squares = [Square(i, j, color) for i in range(ROWS) for j in range(COLS)]
        self.name = name

    def __str__(self):
        return self.name

    def colors(self):
        """
        returns a tuple of colors to use before
        as the 'before' movement when changing colors
        """
        return tuple(self.squares[i].color for i in range(N ** 2))

    def GL_Draw_Face_Front(self):
        for square in self.squares:
            square.GLDraw_Square_Front()

    def GL_Draw_Face_Right(self):
        for square in self.squares:
            square.GLDraw_Square_Right()

    def GL_Draw_Face_Top(self):
        for square in self.squares:
            square.GLDraw_Square_Top()
