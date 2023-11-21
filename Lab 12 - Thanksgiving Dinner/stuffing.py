from random import choice

from plate_decorator import PlateDecorator


class Stuffing(PlateDecorator):

  def description(self):
    adjective = choice(["Vegan", "Spicy", "Bread", "Herb", "Cranberry"])
    if super().count() == 0: 
      return f"{super().description()} with {adjective} Stuffing"
    return f"{super().description()} and {adjective} Stuffing"

  def area(self):
    return super().area() - 18

  def weight(self):
    return super().weight() - 7

  def count(self):
    return super().count() + 1
