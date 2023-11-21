from random import choice

from plate_decorator import PlateDecorator


class Potatoes(PlateDecorator):
  
  def description(self):
    adjective = choice(["Mashed", "Scalloped", "Raw", "Sweet", "Baked"])
    if super().count() == 0: 
      return f"{super().description()} with {adjective} Potatoes"
    return f"{super().description()} and {adjective} Potatoes"

  def area(self):
    return super().area() - 18

  def weight(self):
    return super().weight() - 6

  def count(self):
    return super().count() + 1
