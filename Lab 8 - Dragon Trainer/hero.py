from entity import Entity
from random import randint


class Hero(Entity):

  def basic_attack(self, other):
    damage = randint(1, 6) + randint(1, 6)
    other.take_damage(damage)
    return f"\nYou slash the {other.name} with your sword for {damage} damage!"

  def special_attack(self, other):
    damage = randint(1, 12)
    other.take_damage(damage)
    return f"\nYou shoot the {other.name} with your arrow for {damage} damage!"
