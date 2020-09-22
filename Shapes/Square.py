from OpenGL.GL import glBegin, glColor3fv, glEnd
from OpenGL.raw.GL.VERSION.GL_1_0 import glVertex3f
from OpenGL.raw.GL.VERSION.GL_4_0 import GL_QUADS

from Config import N


class Square:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def __str__(self):
        return "{} {}".format(self.row, self.col)

    def GLDraw_Square_Front(self):
        j = self.row
        i = self.col
        glColor3fv(self.color)
        glBegin(GL_QUADS)
        glVertex3f(i, N - j - 1, N)
        glVertex3f(i, N - j, N)
        glVertex3f(i + 1, N - j, N)
        glVertex3f(i + 1, N - j - 1, N)
        glEnd()

    def GLDraw_Square_Right(self):
        j = self.row
        i = self.col
        glColor3fv(self.color)
        glBegin(GL_QUADS)
        glVertex3f(N, N - j - 1, N - i)
        glVertex3f(N, N - j, N - i)
        glVertex3f(N, N - j, N - i - 1)
        glVertex3f(N, N - j - 1, N - i - 1)
        glEnd()

    def GLDraw_Square_Top(self):
        j = self.row
        i = self.col
        glColor3fv(self.color)
        glBegin(GL_QUADS)
        glVertex3f(i, N, j)
        glVertex3f(i, N, j + 1)
        glVertex3f(i + 1, N, j + 1)
        glVertex3f(i + 1, N, j)
        glEnd()
