from random import randint

"""
6 faces,
Each face has 16 squares
"""
#testing with 4x4 cube, hopes that i may work for higher level cubes
n = 4
rows = n
cols = n

#define colours (useful for pygame implementation)
Orange = 'O'#(255, 130, 0) #Front
white = 'W'#(255, 255, 255) #Bottom
blue = 'B'#(0, 0, 255) # Right
red = 'R'#(255, 0, 0) # Back
green = 'G'#(0, 255, 0) # Left
yellow = 'Y'#(255, 255, 0) # Top

class Square():
    """These square's colours will be changable by certain face functions"""

    def __init__(self, row, col, colour):
        """initially assigned colour by the face"""
        self.row = row
        self.col = col
        self.colour = colour

    def __str__(self):
        "this is the name of this object!"
        return self.row + self.col

class Face:

    def __init__(self,name, colour):
        self.squares = []
        self.name = name
        self.colour = colour
        for i in range(rows): #creation of individual squares
            for j in range(cols):
                self.squares.append(Square(str(i), str(j), self.colour))
        self.colour = None #removing attribute to ensure no confusion later

    def __str__(self): #could be used in pygame
        return self.name

    def colours(self):
        """returns a tupled list of colours to use before
        as the 'before' movement when changing colours"""
        dummylist = []
        for i in range(0, n**2):
            dummylist.append(self.squares[i].colour)
        dummylist = tuple(dummylist)
        return dummylist

    def face_rotation(self, direction):
        pass

class Cube(object):

    def __init__(self):
        self.faces = []
        for i in [('Front', Orange), ('Back', red), ('Left', green), ('Right', blue), ('Top', yellow ), ('Bottom', white)]:
            self.faces.append(Face(i[0], i[1]))

    def print_cube(self):
        """Displays faces with list of their colours"""
        for i in range(0, 6):
            print(self.faces[i])
            print(self.faces[i].colours())

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
            for i in range(0,3): #clockwise turn
                self.rotation('right', pos)

        if direction == 'up':
            for i in range(0, n):
                Front.squares[pos + i*n].colour, Top.squares[pos + i*n].colour, Back.squares[pos + i*n].colour, Bottom.squares[pos + i*n].colour = Bottom.squares[pos + i*n].colour, Front.squares[pos + i*n].colour, Top.squares[pos + i*n].colour, Back.squares[pos + i*n].colour

            if pos == 0:
                self.Face_Spin_Anticlockwise(2) #left face
            elif pos == n-1:
                for i in range(0, 3): # clockwise turn
                    self.Face_Spin_Anticlockwise(3)

        if direction == 'down':
            for i in range(0, 3):
                self.rotation('up', pos)

    def Face_Spin_Anticlockwise(self, face):
        """this deals with the complicated spinning faces"""

        dummylist = tuple(self.faces[face].colours()) #list of squares on top
        for j in range(0, n):
            placeholder = 3 - j
            for i in range(0, n):
                self.faces[face].squares[i + 4*j].colour = dummylist[placeholder]
                if placeholder > 12:
                    placeholder -= 12
                else:
                    placeholder += 4

    def scramble(self):
        "I have defined 4*n moves"
        moves = ['up', 'down', 'right', 'left']
        for i in range(0, 100):
            x = randint(0, 3)
            y = randint(0, n-1)
            self.rotation(moves[x], y)



Rubiks = Cube() #create cube

 #for readability of code
Front, Back, Left, Right, Top, Bottom = Rubiks.faces[0], Rubiks.faces[1], Rubiks.faces[2], Rubiks.faces[3], Rubiks.faces[4], Rubiks.faces[5]

Rubiks.print_cube()
Rubiks.scramble()
Rubiks.print_cube()

solved = False
count  = 0

 """test area"""
#
# position = 0 #[0 to n]
#
# Rubiks.rotation('right', 0)
# Rubiks.rotation('left', 3)
#
# Rubiks.rotation('up', 0)
# Rubiks.rotation('down', 0)
#
# Rubiks.print_cube()

# lists16 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p']
