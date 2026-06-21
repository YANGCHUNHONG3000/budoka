# Packages
from globals import *

# Read key from keyboard
def read_key():
  ch = -1
  while ch == -1: ch = screen.getch()
  return ch

# Process user command
def parse_command():
  ch = read_key()
  if ch in [ord(c) for c in 'hjklyubn']: move(ch)
  if chr(ch) in 'HJKLYUBN': run(chr(ch))
  elif ch == ord('>') and game['dungeon'][game['player']['y']][game['player']['x']] == STAIRS:
    game['level'] += 1
    make_level()
  elif ch == ord('q'):
    curses.endwin()
    sys.exit()
