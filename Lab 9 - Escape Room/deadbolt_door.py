from door import Door
from random import choice


class DeadboltDoor(Door):

  def __init__(self):
    self.deadbolt1 = choice([True, False])
    self.deadbolt2 = choice([True, False])

  def examine_door(self):
    return "A door with two deadbolts. Both need to be unlocked to open the door, but you can’t tell if each one is locked or unlocked."

  def menu_options(self):
    return "1. Toggle bolt 1\n2. Toggle bolt 2\n"

  def get_menu_max(self):
    return 2

  def attempt(self, option):
    if option == 1:
      self.deadbolt1 = not self.deadbolt1
      return "You toggle the first deadbolt."
    elif option == 2:
      self.deadbolt2 = not self.deadbolt2
      return "You toggle the second deadbolt."
    return "Invalid option."

  def is_unlocked(self):
    return self.deadbolt1 and self.deadbolt2 

  def clue(self):
    if self.deadbolt1 != self.deadbolt2:
      return "You jiggle the door...it seems like one of the bolts is unlocked."
    return "It seems completely locked."

  def success(self):
    return "Congratulations, you unlocked both deadbolts and opened the door.\n"
