"""
6 faces,
Each face has 16 squares
"""
#testing with 4x4 cube, hopes that i may work for higher level cubes
rows = 4
cols = 4

#define colours (useful for pygame implementation)
Orange = (255, 130, 0) #Front
white = (255, 255, 255) #Bottom
blue = (0, 0, 255) # Right
red = (255, 0, 0) # Back
green = (0, 255, 0) # Left
yellow = (255, 255, 0) # Top

Front, Back, Left, Right, Top, Bottom = 'Front', 'Back', 'Left', 'Right', 'Top', 'Bottom'



class Square():
    """These squares' colours will be changable by certain face functions"""

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
        self.colour = colour # this may be used for winning condition
        for i in range(rows): #creation of individual squares
            for j in range(cols):
                self.squares.append(Square(str(i), str(j), self.colour))

    def __str__(self): #do i need to specify each face?
        return self.name

class Cube(object):

    def __init__(self):
        self.faces = []
        for i in [('Front', Orange), ('Back', red), ('Left', green), ('Right', blue), ('Top', yellow ), ('Bottom', white)]:
            self.faces.append(Face(i[0], i[1]))

    def rotation(self, direction, position):
        """rotations are always relative to the front face,
        this is made possible by rotating all rows/colums in the same direction we affectively change face"""
        if direction == 'right':
            pass
        if direction =='left':
            pass
        if direction == 'up' or 'down':
            pass

Rubiks = Cube() #create cube

#checking we can access each object
# for i in Rubiks.faces:
#     for j in i.squares:
#         print(j.name, end=',')
#     print('')
#
# for i in Rubiks.faces:
#     print(i.name, end='')
#     print(i.colour)

print(Rubiks.faces[0])
print(Front.name)
#print(Front.colour)
