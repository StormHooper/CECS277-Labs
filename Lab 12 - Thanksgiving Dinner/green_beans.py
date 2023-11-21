from random import choice

from plate_decorator import PlateDecorator


class GreenBeans(PlateDecorator):

  def description(self):
    adjective = choice(["Green", "Baked", "Refried", "Chili", "Jelly"])
    if super().count() == 0: 
      return f"{super().description()} with {adjective} Beans"
    return f"{super().description()} and {adjective} Beans"

  def area(self):
    return super().area() - 19

  def weight(self):
    return super().weight() - 8

  def count(self):
    return super().count() + 1
