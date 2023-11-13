from random import randint

from entity import Entity


class Zombie(Entity):
  def __init__(self):
    super().__init__("Flesh Bud Zombie", randint(8,10))

  def attack(self, entity):
    dmg = randint(5, 12)
    entity.take_damage(dmg)
    return f"{self.name} attacks a {entity.name} for {dmg} damage."
