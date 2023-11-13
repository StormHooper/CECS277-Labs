from random import randint

from entity import Entity


class Skeleton(Entity):
  def __init__(self):
    super().__init__("Spooky Scary Skeleton", randint(6,10))

  def attack(self, entity):
    dmg = randint(6, 10)
    entity.take_damage(dmg)
    return f"{self.name} attacks a {entity.name} for {dmg} damage."
