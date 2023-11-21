# Name: Tyler Pham and Matthew Samar
# Date: 21 November 2023
# Description: Thanksgiving Dinner. Player chooses a plate, then takes some food.
# Depending on the plate, the player can take more or less food.
# If the player takes too much, their plate will spill.

from check_input import get_int_range
from green_beans import GreenBeans
from large_plate import LargePlate
from pie import Pie
from potatoes import Potatoes
from small_plate import SmallPlate
from stuffing import Stuffing
from turkey import Turkey


def examine_plate(p):
  '''
  Prints description of plate and analyzes the weight and area to give hints.
  Returns True if there is still leftover weight or area, else it returns False.
  '''
  print(p.description())

  if p.weight() >= 13:
    print("This plate is carrying the food well.")
  elif 12 > p.weight() > 7:
    print("This plate can carry a little more food.")
  elif 6 > p.weight() > 1:
    print("This plate is feeling heavy!")

  if p.area() >= 41:
    print("This plate has a lot of space for more.")
  elif 40 > p.area() > 21:
    print("This plate can fit a little more food.")
  elif 21 > p.area() > 1:
    print("This plate is looking full!")

  if p.area() < 1 or p.weight() < 1:
    print(
        "Oh no, you put too much and dropped the plate! Just big and greedy!")
    return True
  return False


def main():
  print("- Thanksgiving Dinner -\n"
        "Serve yourself as much food as you like from the buffet, "
        "but make sure that your plate will hold without spilling everywhere!")
  plate_choice = get_int_range(
      "Choose a plate:\n1. Small Sturdy Plate \n2. Large Flimsy Plate\n", 1, 2)
  plate = SmallPlate() if plate_choice == 1 else LargePlate()

  while True:
    food_choice = get_int_range(
        "1. Turkey\n2. Stuffing\n3. Potatoes\n4. Green Beans\n5. Pie\n6. Quit\n",
        1, 6)
    if food_choice == 1:
      plate = Turkey(plate)
    elif food_choice == 2:
      plate = Stuffing(plate)
    elif food_choice == 3:
      plate = Potatoes(plate)
    elif food_choice == 4:
      plate = GreenBeans(plate)
    elif food_choice == 5:
      plate = Pie(plate)
    else:
      break
    if examine_plate(plate):
      break

  if plate.weight() > 0 and plate.area() > 0:
    print(f"Good job! You made it to the table with {plate.count()} items!\n"
          f"There was still {plate.area()} square inches left on your plate.\n"
          f"Your plate could have held {plate.weight()} more ounces of food.\n"
          "Don't worry, you can always go back for more. Happy Thanksgiving!")

main()
