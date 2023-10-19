from random import randint

from door import Door


class BasicDoor(Door):

  def __init__(self):
    self.state = randint(1, 2)
    self.move = 0

  def examine_door(self):
    return "A door that is either pushed or pulled."

  def menu_options(self):
    return "1. Push \n2. Pull\n"

  def get_menu_max(self):
    return 2

  def attempt(self, option):
    self.move = option
    if option == 1:
      return "You push the door."
    return "You pull the door."

  def is_unlocked(self):
    return self.state == self.move

  def clue(self):
    return "Try the other way."

  def success(self):
    return "Congratulations, wow, you swung a door open, so impressive.\n"
