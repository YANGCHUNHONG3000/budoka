# Packages
import sys
import math
import curses
from random import randrange, choice

# Constants
ROWS = 24
COLS = 80

MAXROOMS = 9
MINROOMS = 6

MAX_ROOM_WIDTH = 18
MIN_ROOM_WIDTH = 5
MAX_ROOM_HEIGHT = 6
MIN_ROOM_HEIGHT = 4

SECTORS_ROW1_OFFSET_MAX = 26
SECTORS_ROW1_OFFSET_MIN = 10
SECTORS_ROW2_OFFSET_MAX = 45
SECTORS_ROW2_OFFSET_MIN = 32
SECTORS_ROW3_OFFSET_MAX = 69
SECTORS_ROW3_OFFSET_MIN = 54

SECTORS_COL1_OFFSET_MAX = 9
SECTORS_COL1_OFFSET_MIN = 2
SECTORS_COL2_OFFSET_MAX = 16
SECTORS_COL2_OFFSET_MIN = 9
SECTORS_COL3_OFFSET_MAX = 23
SECTORS_COL3_OFFSET_MIN = 16

DOOR = '+'
EMPTY = ' '
FLOOR = '.'
V_WALL = '|'
H_WALL = '-'
STAIRS = '%'
PLAYER = '@'
PASSAGE = '#'

EMEMIES = {
 'A': 'Aikido',
 'B': 'Boxing',
 'C': 'Capoeira',
 'G': 'Grappling',
 'H': 'Hapkido',
 'J': 'Judo',
 'K': 'Karate',
 'M': 'Muay Thai',
 'R': 'Russian style',
 'S': 'Sumo',
 'T': 'Taekwondo',
 'W': 'Wing Chun',
}

RANKS = {
  '1': '5 kyu',
  '2': '4 kyu',
  '3': '3 kyu',
  '4': '2 kyu',
  '5': '1 kyu',
  '6': '1 dan',
  '7': '2 dan',
  '8': '3 dan',
  '9': '4 dan',
  '10': '5 dan',
  '11': '6 dan',
  '12': '7 dan',
  '13': '8 dan',
  '14': '9 dan',
}

MAX_LEVEL = len(RANKS)

# Variables
game = {
  'dungeon': [[' ']*COLS for i in range(ROWS)],
  'rooms': [],
  'visited_tiles': [],
  'level': 1,
  'player': {
    'y': 0,
    'x': 0,
    'hp': 2,
    'attack': 1,
    'defense': 1,
    'level': 1,
    'sensitivity': False,
    'aggravate': False
  },
  'enemies': []
}

# Curses screen
screen = curses.initscr()
screen.nodelay(1)
curses.noecho()
curses.raw()
screen.keypad(1)
curses.start_color()
curses.use_default_colors()

# Functions
from colors import *
from dice import *
from room import *
from enemies import *
from level import *
from move import *
from command import *
from render import *
