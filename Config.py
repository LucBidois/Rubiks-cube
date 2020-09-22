# testing with 4x4 cube (works for nxn)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024

N = 4
ROWS = N
COLS = N

# define colors (useful for pygame implementation)
COLORS = {
    "red": (0.5, 0, 0),  # (255, 0, 0) # Back
    "orange": (1.0, 0.5, 0),  # (255, 130, 0) # Front
    "yellow": (0.7, 0.7, 0),  # (255, 255, 0) # Top
    "green": (0, 0.5, 0),  # (0, 255, 0) # Left
    "blue": (0, 0, 0.5),  # (0, 0, 255) # Right
    "white": (0.7, 0.7, 0.7),  # (255, 255, 255) # Bottom
    "black": (0, 0, 0),
}
