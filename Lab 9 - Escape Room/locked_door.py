from door import Door
from random import randint


class LockedDoor(Door):

  def __init__(self):
    self.state = randint(1, 3)
    self.move = 0

  def examine_door(self):
    return "A locked door. Look around for the key."

  def menu_options(self):
    return "1. Look under the mat \n2. Look under the flower pot \n3. Look under the fake rock.\n"

  def get_menu_max(self):
    return 3

  def attempt(self, option):
    self.move = option
    if option == 1:
      return "You look under the mat."
    elif option == 2:
      return "You look under the flower pot."
    return "You look under the fake rock."

  def is_unlocked(self):
    return self.state == self.move

  def clue(self):
    return "Look somewhere else."

  def success(self):
    return "Congratulations, you found the key and opened the door.\n"
