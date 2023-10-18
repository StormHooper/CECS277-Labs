from door import Door
from random import choice


class CodeDoor(Door):

  def __init__(self):
    self.code = [choice(["X","O"]) for x in range(3)]
    self.guessword = [choice(["X","O"]) for x in range(3)]

  def examine_door(self):
    return "A door with a coded keypad with three characters. Each key toggles a value with an ‘X’ or an ‘O’."

  def menu_options(self):
    return "1. Press key 1 \n2. Press key 2 \n3. Press key 3 \n"

  def get_menu_max(self):
    return 3

  def attempt(self, option):
    if self.guessword[option-1] == "X":
      self.guessword[option-1] = "O"
    elif self.guessword[option-1] == "O":
      self.guessword[option-1] = "X"
    return f"You press key {option}. The keypad states: {''.join(self.guessword)}"

  def is_unlocked(self):
    return self.code == self.guessword

  def clue(self):
    correct = 0
    for c in range(len(self.code)):
      if self.code[c] == self.guessword[c]:
        correct += 1
    return f"{correct} of the correct characters are in the correct position."

  def success(self):
    return "Congratulations, you cracked the code and opened the door.\n"
