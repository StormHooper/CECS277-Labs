from random import randint

from door import Door


class ComboDoor(Door):

  def __init__(self):
    self.state = randint(1, 10)
    self.move = 0

  def examine_door(self):
    return "A door with a combination lock. You can spin the dial to a number 1-10."

  def menu_options(self):
    return "Enter # 1-10: "

  def get_menu_max(self):
    return 10

  def attempt(self, option):
    self.move = option
    return f"You turn the dial to... {option}"

  def is_unlocked(self):
    return self.state == self.move

  def clue(self):
    if self.move > self.state:
      return "Too high."
    return "Too low."

  def success(self):
    return "Congratulations, you found the correct value and opened the door.\n"
