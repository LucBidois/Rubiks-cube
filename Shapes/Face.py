from Config import COLS, N, ROWS
from Shapes.Square import Square


class Face():

    def __init__(self, name, color):
        self.squares = []
        self.name = name
        self.color = color
        for i in range(ROWS):
            for j in range(COLS):
                self.squares.append(Square(i, j, self.color))
        self.color = None  # removing attribute to ensure no confusion later

    def __str__(self):
        return self.name

    def colors(self):
        """returns a tupled list of colors to use before
        as the 'before' movement when changing colors"""
        dummylist = []
        for i in range(0, N ** 2):
            dummylist.append(self.squares[i].color)
        dummylist = tuple(dummylist)
        return dummylist

    def GL_Draw_Face_Front(self):
        for square in self.squares:
            square.GLDraw_Square_Front()

    def GL_Draw_Face_Right(self):
        for square in self.squares:
            square.GLDraw_Square_Right()

    def GL_Draw_Face_Top(self):
        for square in self.squares:
            square.GLDraw_Square_Top()