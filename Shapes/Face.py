from Config import cols, n, rows
from Shapes.Square import Square


class Face():

    def __init__(self, name, colour):
        self.squares = []
        self.name = name
        self.colour = colour
        for i in range(rows):
            for j in range(cols):
                self.squares.append(Square(str(i), str(j), self.colour))
        self.colour = None  # removing attribute to ensure no confusion later

    def __str__(self):
        return self.name

    def colours(self):
        """returns a tupled list of colours to use before
        as the 'before' movement when changing colours"""
        dummylist = []
        for i in range(0, n ** 2):
            dummylist.append(self.squares[i].colour)
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