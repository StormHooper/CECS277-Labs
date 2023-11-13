from random import randint

from entity import Entity
from map import Map


class Hero(Entity):
  def __init__(self, name):
    super().__init__(name, 25)
    self._loc = [0, 0]

  @property
  def loc(self):
    return self._loc

  def attack(self, entity):
    damage = randint(2, 5)
    entity.take_damage(damage)
    return f"{self.name} attacks a {entity.name} for {damage} damage."

  def go_north(self):
    if self.loc[0] > 0:
      self.loc[0] -= 1
      return Map()[self.loc[0]][self.loc[1]]
    return "o"

  def go_south(self):
    if self.loc[0] < len(Map()) - 1:
      self.loc[0] += 1
      return Map()[self.loc[0]][self.loc[1]]
    return "o"

  def go_east(self):
    if self.loc[1] < len(Map()[self.loc[0]]) - 1:
      self.loc[1] += 1
      return Map()[self.loc[0]][self.loc[1]]
    return "o"

  def go_west(self):
    if self.loc[1] > 0:
      self.loc[1] -= 1
      return Map()[self.loc[0]][self.loc[1]]
    return "o"
