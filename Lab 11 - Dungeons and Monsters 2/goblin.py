from random import randint

from entity import Entity


class Goblin(Entity):
  def __init__(self):
    super().__init__("Willem Dafoe (Green Goblin)", randint(8,12))

  def attack(self, entity):
    dmg = randint(6, 12)
    entity.take_damage(dmg)
    return f"{self.name} attacks a {entity.name} for {dmg} damage."
