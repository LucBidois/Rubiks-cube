from random import randint

from OpenGL.GL import glBegin, glEnd
from OpenGL.raw.GL.VERSION.GL_1_0 import GL_LINES, glColor3f, glVertex3f

from Config import COLORS, N
from Shapes.Face import Face


class Cube(object):

    def __init__(self):
        self.faces = [Face('Front', COLORS["orange"]), Face('Back', COLORS["red"]),
                      Face('Left', COLORS["green"]), Face('Right', COLORS["blue"]),
                      Face('Top', COLORS["yellow"]), Face('Bottom', COLORS["white"])]

    def print_cube(self):
        """Displays faces with list of their colors in interpreter"""
        for face in range(0, 6):
            print(self.faces[face])
            for j in range(0, N):
                print(self.faces[face].colors()[4 * j:4 * j + N])

    def rotation(self, direction, pos):
        """rotations are always relative to the front face,
        this is made possible by rotating all rows/columns in the same direction we affectively change face"""

        Front, Back, Left, Right, Top, Bottom = self.faces

        if direction == 'right':
            for i in range(0, N):
                Front.squares[pos * N + i].color, Right.squares[pos * N + i].color, Back.squares[pos * N + i].color, \
                Left.squares[pos * N + i].color = Left.squares[pos * N + i].color, Front.squares[pos * N + i].color, \
                                                   Right.squares[pos * N + i].color, Back.squares[pos * N + i].color

            if pos == 0:
                """rotation of the top face"""
                self.Face_Spin_Anticlockwise(4)

            elif pos == N - 1:
                """bottom face spins clockwise normally"""
                for i in range(0, 3):
                    self.Face_Spin_Anticlockwise(5)

        if direction == 'left':
            for i in range(0, 3):
                self.rotation('right', pos)

        if direction == 'up':
            for i in range(0, N):
                Front.squares[pos + i * N].color, Top.squares[pos + i * N].color, Back.squares[
                    (N ** 2 - 1) - (N * i) - pos].color, Bottom.squares[pos + N * i].color = Bottom.squares[
                                                                                                   pos + i * N].color, \
                                                                                               Front.squares[
                                                                                                   pos + i * N].color, \
                                                                                               Top.squares[
                                                                                                   pos + i * N].color, \
                                                                                               Back.squares[
                                                                                                   (N ** 2 - 1) - (
                                                                                                           N * i) - pos].color

            if pos == 0:
                self.Face_Spin_Anticlockwise(2)  # left face
            elif pos == N - 1:
                for i in range(0, 3):
                    self.Face_Spin_Anticlockwise(3)  # right face

        if direction == 'down':
            for i in range(0, 3):
                self.rotation('up', pos)

    def Face_Spin_Anticlockwise(self, face):
        """this deals with the complicated spinning faces"""

        old_colors = tuple(self.faces[face].colors())  # list of squares on top
        for j in range(0, N):
            color_Index = (N - 1) - j
            for i in range(0, N):
                self.faces[face].squares[i + N * j].color = old_colors[color_Index]
                if color_Index > N * (N - 1):
                    color_Index -= N * (N - 1)
                else:
                    color_Index += N

    def scramble(self):
        "I have defined 4*n moves"
        moves = ['up', 'down', 'right', 'left']
        for i in range(0, 100):
            x = randint(0, 3)
            y = randint(0, N - 1)
            self.rotation(moves[x], y)

    def GL_Draw_Cube(self):
        self.faces[0].GL_Draw_Face_Front()
        self.faces[3].GL_Draw_Face_Right()
        self.faces[4].GL_Draw_Face_Top()
        self.GL_Square_Separation_Lines()

    @staticmethod
    def GL_Square_Separation_Lines():
        glBegin(GL_LINES)
        glColor3f(0.5, 0.5, 0.5)
        for lineIndex in range(1, N):
            # front width
            glVertex3f(0, lineIndex, N)
            glVertex3f(N, lineIndex, N)
            # front height
            glVertex3f(lineIndex, 0, N)
            glVertex3f(lineIndex, N, N)
            # side depth
            glVertex3f(N, lineIndex, 0)
            glVertex3f(N, lineIndex, N)
            # side height
            glVertex3f(N, 0, lineIndex)
            glVertex3f(N, N, lineIndex)
            # top width
            glVertex3f(0, N, lineIndex)
            glVertex3f(N, N, lineIndex)
            # top depth
            glVertex3f(lineIndex, N, 0)
            glVertex3f(lineIndex, N, N)
        glEnd()
