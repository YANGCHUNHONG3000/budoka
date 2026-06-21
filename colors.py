# Globals
from globals import *

# Colors
curses.init_pair(1, curses.COLOR_RED, -1),
curses.init_pair(2, curses.COLOR_CYAN, -1),
curses.init_pair(3, curses.COLOR_BLUE, -1),
curses.init_pair(4, curses.COLOR_GREEN, -1),
curses.init_pair(5, curses.COLOR_BLACK, -1),
curses.init_pair(6, curses.COLOR_WHITE, -1),
curses.init_pair(7, curses.COLOR_YELLOW, -1),
curses.init_pair(8, curses.COLOR_MAGENTA, -1)

# Paint text
def paint(color):
  return {
    'red': curses.color_pair(1),
    'cyan': curses.color_pair(2),
    'blue': curses.color_pair(3),
    'green': curses.color_pair(4),
    'black': curses.color_pair(5),
    'white': curses.color_pair(6),
    'yellow': curses.color_pair(7),
    'magenta': curses.color_pair(8),
    'darkred': curses.color_pair(1) | curses.A_DIM,
    'darkcyan': curses.color_pair(2) | curses.A_DIM,
    'darkblue': curses.color_pair(3) | curses.A_DIM,
    'darkgreen': curses.color_pair(4) | curses.A_DIM,
    'darkblack': curses.color_pair(5) | curses.A_DIM,
    'darkwhite': curses.color_pair(6) | curses.A_DIM,
    'darkyellow': curses.color_pair(7) | curses.A_DIM,
    'darkmagenta': curses.color_pair(8) | curses.A_DIM
  }[color]
