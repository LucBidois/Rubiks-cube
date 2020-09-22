import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from Config import n
from Shapes.Cube import Cube


# now that the cube is created, the pygame code follows
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    """GL Initialising function area"""
    gluPerspective(45, (display[0] / display[1]), 0.1, 500)

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glTranslate(0, 0, -20)
    glRotate(35, 1, -1, 0)

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

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        """GL Function drawings"""
        Rubiks.GL_Draw_Cube()

        pygame.display.flip()
        pygame.time.wait(10)


Rubiks = Cube()
Front, Back, Left, Right, Top, Bottom = Rubiks.faces[0], Rubiks.faces[1], Rubiks.faces[2], Rubiks.faces[3], \
                                        Rubiks.faces[4], Rubiks.faces[5]
main()
