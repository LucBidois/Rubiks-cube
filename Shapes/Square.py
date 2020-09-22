from OpenGL.GL import glBegin, glColor3fv, glEnd
from OpenGL.raw.GL.VERSION.GL_1_0 import glVertex3f
from OpenGL.raw.GL.VERSION.GL_4_0 import GL_QUADS

from Config import Color, N


class Square:

    def __init__(self, row: int, col: int, color: Color):
        self.row = row
        self.col = col
        self.color = color

    def __str__(self):
        return "{} {}".format(self.row, self.col)

    @staticmethod
    def __GLDraw_Square_Front(i: int, j: int) -> None:
        glVertex3f(i, N - j - 1, N)
        glVertex3f(i, N - j, N)
        glVertex3f(i + 1, N - j, N)
        glVertex3f(i + 1, N - j - 1, N)

    @staticmethod
    def __GLDraw_Square_Right(i: int, j: int) -> None:
        glVertex3f(N, N - j - 1, N - i)
        glVertex3f(N, N - j, N - i)
        glVertex3f(N, N - j, N - i - 1)
        glVertex3f(N, N - j - 1, N - i - 1)

    @staticmethod
    def __GLDraw_Square_Top(i: int, j: int) -> None:
        glVertex3f(i, N, j)
        glVertex3f(i, N, j + 1)
        glVertex3f(i + 1, N, j + 1)
        glVertex3f(i + 1, N, j)

    def GLDraw_Square(self, orientation: str) -> None:
        orientation = orientation.lower()
        j, i = self.row, self.col
        glColor3fv(self.color)
        glBegin(GL_QUADS)
        if orientation == "front":
            self.__GLDraw_Square_Front(i, j)
        elif orientation == "right":
            self.__GLDraw_Square_Right(i, j)
        elif orientation == "top":
            self.__GLDraw_Square_Top(i, j)
        glEnd()
