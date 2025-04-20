"""
Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
"""

# import module 

from random import randint

NUM_SIDES = 6 
# Write a funtion
def roll_dice():
  # randint() already returns int
  die_1 = randint(1, NUM_SIDES)
  die_2 = randint(1, NUM_SIDES)
  total = die_1 + die_2 
  print(f"🎲Total of two dice = {total}")

def main()->None:
  die_1 = 10
  print(f"🔢die_1 in main() starts as {die_1}")
  
  for _ in range(3):
     roll_dice()
 
  print(f"🔁die_1 in main() is {die_1} ")

if __name__ == "__main__":
  main()


