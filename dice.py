# Globals
from globals import *

# Toss a coin
def coin_toss():
  return randrange(0, 2)

# Roll dice
def roll_dice(times, sides):
  value = 0
  for time in range(times):
    value += randrange(1, sides+1)
  return value
