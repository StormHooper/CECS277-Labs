from random import choice

from plate_decorator import PlateDecorator


class Turkey(PlateDecorator):

  def description(self):
    adjective = choice(["Grilled", "Stuffed", "Roasted", "Dry", "Fried"])
    if super().count() == 0: 
      return f"{super().description()} with {adjective} Turkey"
    return f"{super().description()} and {adjective} Turkey"

  def area(self):
    return super().area() - 15

  def weight(self):
    return super().weight() - 4

  def count(self):
    return super().count() + 1
