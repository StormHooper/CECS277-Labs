from entity import Entity
from random import randint


class Dragon(Entity):

  def basic_attack(self, other):
    damage = randint(3, 7)
    other.take_damage(damage)
    return f"{self.name} smashes you with its tail for {damage} damage!\n"

  def special_attack(self, other):
    damage = randint(4, 8)
    other.take_damage(damage)
    return f"{self.name} slashes you with its claws for {damage} damage!\n"
