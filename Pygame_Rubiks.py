from random import randint
import pygame
import time
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

display_width = 800
display_height = 600

#testing with 4x4 cube, hopes that it may work for higher level cubes
n = 4
rows = n
cols = n

#define colours (useful for pygame implementation)
Orange = (1.0, 0.5, 0) #(255, 130, 0) #Front
white = (0.7, 0.7, 0.7)    #(255, 255, 255) #Bottom
blue = (0, 0, 0.5)     #(0, 0, 255) # Right
red = (0.5, 0, 0)      #(255, 0, 0) # Back
green = (0, 0.5, 0)    #(0, 255, 0) # Left
yellow = (0.7, 0.7, 0)   #(255, 255, 0) # Top

black = (0, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height)) #set resolution, (width, height)
pygame.display.set_caption('Rubiks Cube') #Name displayed on bar
clock = pygame.time.Clock()#define game clock


class Square():
    """These square's colours will be changable by certain face functions"""

    def __init__(self, row, col, colour):
        """initially assigned colour by the face"""
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
        glVertex3f(i, n-j-1, n)
        glVertex3f(i, n-j, n)
        glVertex3f(i+1, n-j, n)
        glVertex3f(i+1, n-j-1, n)
        glEnd()

    def GLDraw_Square_Right(self):
        j = int(self.row)
        i = int(self.col)
        glColor3fv(self.colour)
        glBegin(GL_QUADS)
        glVertex3f(n, n-j-1, n-i)
        glVertex3f(n, n-j, n-i)
        glVertex3f(n, n-j, n-i-1)
        glVertex3f(n, n-j-1, n-i-1)
        glEnd()

    def GLDraw_Square_Top(self):
        j = int(self.row)
        i = int(self.col)
        glColor3fv(self.colour)
        glBegin(GL_QUADS)
        glVertex3f(i, n, j)
        glVertex3f(i, n, j+1)
        glVertex3f(i+1, n, j+1)
        glVertex3f(i+1, n, j)
        glEnd()


class Face():

    def __init__(self,name, colour):
        self.squares = []
        self.name = name
        self.colour = colour
        for i in range(rows): #creation of individual squares
            for j in range(cols):
                self.squares.append(Square(str(i), str(j), self.colour))
        self.colour = None #removing attribute to ensure no confusion later

    def __str__(self): #could be used in pygame?
        return self.name

    def colours(self):
        """returns a tupled list of colours to use before
        as the 'before' movement when changing colours"""
        dummylist = []
        for i in range(0, n**2):
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



class Cube(object):

    def __init__(self):
        self.faces = []
        for i in [('Front', Orange), ('Back', red), ('Left', green), ('Right', blue), ('Top', yellow ), ('Bottom', white)]:
            self.faces.append(Face(i[0], i[1]))

    def print_cube(self):
        """Displays faces with list of their colours"""
        for face in range(0, 6):
            print(self.faces[face])
            for j in range(0, n):
                print(self.faces[face].colours()[4*j:4*j + n])

    def rotation(self, direction, pos):
        """rotations are always relative to the front face,
        this is made possible by rotating all rows/colums in the same direction we affectively change face"""

        if direction == 'right':
            for i in range(0, n):
                Front.squares[pos*n + i].colour, Right.squares[pos*n + i].colour, Back.squares[pos*n + i].colour, Left.squares[pos*n + i].colour = Left.squares[pos*n + i].colour, Front.squares[pos*n + i].colour, Right.squares[pos*n + i].colour, Back.squares[pos*n + i].colour

            if pos == 0:
                """rotation of the top face"""
                self.Face_Spin_Anticlockwise(4)

            elif pos == n-1:
                """bottom face spins clockwise normally"""
                for i in range(0, 3):
                    self.Face_Spin_Anticlockwise(5)

        if direction =='left':
            for i in range(0,3):
                self.rotation('right', pos)

        if direction == 'up':
            for i in range(0, n):
                Front.squares[pos + i*n].colour, Top.squares[pos + i*n].colour, Back.squares[(n**2-1) - (n*i) - pos].colour, Bottom.squares[pos + n*i].colour = Bottom.squares[pos + i*n].colour, Front.squares[pos + i*n].colour, Top.squares[pos + i*n].colour, Back.squares[(n**2-1) - (n*i) - pos].colour

            if pos == 0:
                self.Face_Spin_Anticlockwise(2) #left face
            elif pos == n-1:
                for i in range(0, 3):
                    self.Face_Spin_Anticlockwise(3) #right face

        if direction == 'down':
            for i in range(0, 3):
                self.rotation('up', pos)

    def Face_Spin_Anticlockwise(self, face):
        """this deals with the complicated spinning faces"""

        old_Colours = tuple(self.faces[face].colours()) #list of squares on top
        for j in range(0, n):
            colour_Index = (n-1) - j
            for i in range(0, n):
                self.faces[face].squares[i + n*j].colour = old_Colours[colour_Index]
                if colour_Index > n*(n-1):
                    colour_Index -= n*(n-1)
                else:
                    colour_Index += n

    def scramble(self):
        "I have defined 4*n moves"
        moves = ['up', 'down', 'right', 'left']
        for i in range(0, 100):
            x = randint(0, 3)
            y = randint(0, n-1)
            self.rotation(moves[x], y)

    def GL_Draw_Cube(self):
        self.faces[0].GL_Draw_Face_Front()
        self.faces[3].GL_Draw_Face_Right()
        self.faces[4].GL_Draw_Face_Top()
        self.GL_Square_Sepearation_Lines()

    def GL_Square_Sepearation_Lines(self):
        glBegin(GL_LINES)
        glColor3f(0.5,0.5,0.5)
        for lineIndex in range(1, n):
            #front width
            glVertex3f(0, lineIndex, n)
            glVertex3f(n, lineIndex, n)
            #front height
            glVertex3f(lineIndex, 0, n)
            glVertex3f(lineIndex, n, n)
            #side depth
            glVertex3f(n, lineIndex, 0)
            glVertex3f(n, lineIndex, n)
            #side height
            glVertex3f(n, 0, lineIndex)
            glVertex3f(n, n, lineIndex)
            #top width
            glVertex3f(0, n, lineIndex)
            glVertex3f(n, n, lineIndex)
            #top depth
            glVertex3f(lineIndex, n, 0)
            glVertex3f(lineIndex, n, n)
        glEnd()

#now that the cube is created, the pygame code follows

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    """GL Initialising function area"""
    gluPerspective(45, (display[0]/display[1]), 0.1, 500)

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glTranslate(0, 0, -20)
    glRotate(35, 1, -1,0)

    x = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                print(event)
                print(x)

                if event.key == pygame.K_RETURN:
                    Rubiks.scramble()

                if event.key == pygame.K_KP_PLUS:
                    x += 1
                    if x >= n:
                        x -= 1

                if event.key == pygame.K_KP_MINUS:
                    x -= 1
                    if x < 0:
                        x += 1

                if event.key == pygame.K_LEFT:
                    Rubiks.rotation('left', x)

                if event.key == pygame.K_RIGHT:
                    Rubiks.rotation('right', x)

                if event.key == pygame.K_UP:
                    Rubiks.rotation('up', x)

                if event.key == pygame.K_DOWN:
                    Rubiks.rotation('down', x)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # clear frame to draw on top (specifically the things we have specified)

        """GL Function drawings"""
        Rubiks.GL_Draw_Cube()

        """GL Test drawings"""


        #glFlush() #rushes things along (even if images are not finished)
        pygame.display.flip()
        pygame.time.wait(10)

Rubiks = Cube() #create cube
Front, Back, Left, Right, Top, Bottom = Rubiks.faces[0], Rubiks.faces[1], Rubiks.faces[2], Rubiks.faces[3], Rubiks.faces[4], Rubiks.faces[5]

main()
