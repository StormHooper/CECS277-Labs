from random import choice

from plate_decorator import PlateDecorator


class Pie(PlateDecorator):

  def description(self):
    adjective = choice(["Apple", "Pumpkin", "Pecan", "Chicken Pot", "Pie-Flavored"])
    if super().count() == 0: 
      return f"{super().description()} with {adjective} Pie"
    return f"{super().description()} and {adjective} Pie"

  def area(self):
    return super().area() - 19

  def weight(self):
    return super().weight() - 8

  def count(self):
    return super().count() + 1
