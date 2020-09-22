import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import DOUBLEBUF, OPENGL

from Config import ASPECT_RATIO, DIMENSIONS, N
from Shapes.Cube import Cube


# now that the cube is created, the pygame code follows
def main():
    pygame.init()
    pygame.display.set_mode(DIMENSIONS, DOUBLEBUF | OPENGL)

    """GL Initialising function area"""
    gluPerspective(45, ASPECT_RATIO, 0.1, 500)

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glTranslate(0, 0, -20)
    glRotate(35, 1, -1, 0)

    position = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                print(event)
                print(position)

                if event.key == pygame.K_RETURN:
                    Rubiks.scramble()

                if event.key == pygame.K_KP_PLUS:
                    position = (position + 1) % N

                if event.key == pygame.K_KP_MINUS:
                    position = (position - 1) % N

                if event.key == pygame.K_LEFT:
                    Rubiks.rotation('left', position)

                if event.key == pygame.K_RIGHT:
                    Rubiks.rotation('right', position)

                if event.key == pygame.K_UP:
                    Rubiks.rotation('up', position)

                if event.key == pygame.K_DOWN:
                    Rubiks.rotation('down', position)

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        """GL Function drawings"""
        Rubiks.GL_Draw_Cube()

        pygame.display.flip()
        pygame.time.wait(10)


Rubiks = Cube()

if __name__ == "__main__":
    main()
