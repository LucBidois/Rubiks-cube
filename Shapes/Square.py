from OpenGL.GL import glBegin, glColor3fv, glEnd
from OpenGL.raw.GL.VERSION.GL_1_0 import glVertex3f
from OpenGL.raw.GL.VERSION.GL_4_0 import GL_QUADS

from Config import n


class Square():

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour

    def __str__(self):
        return self.row + self.col

    def GLDraw_Square_Front(self):
        j = int(self.row)
        i = int(self.col)
        glColor3fv(self.colour)
        glBegin(GL_QUADS)
        glVertex3f(i, n - j - 1, n)
        glVertex3f(i, n - j, n)
        glVertex3f(i + 1, n - j, n)
        glVertex3f(i + 1, n - j - 1, n)
        glEnd()

    def GLDraw_Square_Right(self):
        j = int(self.row)
        i = int(self.col)
        glColor3fv(self.colour)
        glBegin(GL_QUADS)
        glVertex3f(n, n - j - 1, n - i)
        glVertex3f(n, n - j, n - i)
        glVertex3f(n, n - j, n - i - 1)
        glVertex3f(n, n - j - 1, n - i - 1)
        glEnd()

    def GLDraw_Square_Top(self):
        j = int(self.row)
        i = int(self.col)
        glColor3fv(self.colour)
        glBegin(GL_QUADS)
        glVertex3f(i, n, j)
        glVertex3f(i, n, j + 1)
        glVertex3f(i + 1, n, j + 1)
        glVertex3f(i + 1, n, j)
        glEnd()