from random import randint

from OpenGL.GL import glBegin, glEnd
from OpenGL.raw.GL.VERSION.GL_1_0 import GL_LINES, glColor3f, glVertex3f

from Config import COLORS, n
from Pygame_Rubiks import Back, Bottom, Front, Left, Right, Top
from Shapes.Face import Face


class Cube(object):

    def __init__(self):
        self.faces = []
        for i in [('Front', COLORS["orange"]), ('Back', COLORS["red"]),
                  ('Left', COLORS["green"]), ('Right', COLORS["blue"]),
                  ('Top', COLORS["yellow"]), ('Bottom', COLORS["white"])]:
            self.faces.append(Face(i[0], i[1]))

    def print_cube(self):
        """Displays faces with list of their colours in interpreter"""
        for face in range(0, 6):
            print(self.faces[face])
            for j in range(0, n):
                print(self.faces[face].colours()[4 * j:4 * j + n])

    def rotation(self, direction, pos):
        """rotations are always relative to the front face,
        this is made possible by rotating all rows/colums in the same direction we affectively change face"""

        if direction == 'right':
            for i in range(0, n):
                Front.squares[pos * n + i].colour, Right.squares[pos * n + i].colour, Back.squares[pos * n + i].colour, \
                Left.squares[pos * n + i].colour = Left.squares[pos * n + i].colour, Front.squares[pos * n + i].colour, \
                                                   Right.squares[pos * n + i].colour, Back.squares[pos * n + i].colour

            if pos == 0:
                """rotation of the top face"""
                self.Face_Spin_Anticlockwise(4)

            elif pos == n - 1:
                """bottom face spins clockwise normally"""
                for i in range(0, 3):
                    self.Face_Spin_Anticlockwise(5)

        if direction == 'left':
            for i in range(0, 3):
                self.rotation('right', pos)

        if direction == 'up':
            for i in range(0, n):
                Front.squares[pos + i * n].colour, Top.squares[pos + i * n].colour, Back.squares[
                    (n ** 2 - 1) - (n * i) - pos].colour, Bottom.squares[pos + n * i].colour = Bottom.squares[
                                                                                                   pos + i * n].colour, \
                                                                                               Front.squares[
                                                                                                   pos + i * n].colour, \
                                                                                               Top.squares[
                                                                                                   pos + i * n].colour, \
                                                                                               Back.squares[
                                                                                                   (n ** 2 - 1) - (
                                                                                                           n * i) - pos].colour

            if pos == 0:
                self.Face_Spin_Anticlockwise(2)  # left face
            elif pos == n - 1:
                for i in range(0, 3):
                    self.Face_Spin_Anticlockwise(3)  # right face

        if direction == 'down':
            for i in range(0, 3):
                self.rotation('up', pos)

    def Face_Spin_Anticlockwise(self, face):
        """this deals with the complicated spinning faces"""

        old_Colours = tuple(self.faces[face].colours())  # list of squares on top
        for j in range(0, n):
            colour_Index = (n - 1) - j
            for i in range(0, n):
                self.faces[face].squares[i + n * j].colour = old_Colours[colour_Index]
                if colour_Index > n * (n - 1):
                    colour_Index -= n * (n - 1)
                else:
                    colour_Index += n

    def scramble(self):
        "I have defined 4*n moves"
        moves = ['up', 'down', 'right', 'left']
        for i in range(0, 100):
            x = randint(0, 3)
            y = randint(0, n - 1)
            self.rotation(moves[x], y)

    def GL_Draw_Cube(self):
        self.faces[0].GL_Draw_Face_Front()
        self.faces[3].GL_Draw_Face_Right()
        self.faces[4].GL_Draw_Face_Top()
        self.GL_Square_Sepearation_Lines()

    def GL_Square_Sepearation_Lines(self):
        glBegin(GL_LINES)
        glColor3f(0.5, 0.5, 0.5)
        for lineIndex in range(1, n):
            # front width
            glVertex3f(0, lineIndex, n)
            glVertex3f(n, lineIndex, n)
            # front height
            glVertex3f(lineIndex, 0, n)
            glVertex3f(lineIndex, n, n)
            # side depth
            glVertex3f(n, lineIndex, 0)
            glVertex3f(n, lineIndex, n)
            # side height
            glVertex3f(n, 0, lineIndex)
            glVertex3f(n, n, lineIndex)
            # top width
            glVertex3f(0, n, lineIndex)
            glVertex3f(n, n, lineIndex)
            # top depth
            glVertex3f(lineIndex, n, 0)
            glVertex3f(lineIndex, n, n)
        glEnd()