from random import randint

from entity import Entity


class EasySkeleton(Entity):
  def __init__(self):
    super().__init__("Skeleton", randint(3,4))

  def attack(self, entity):
    dmg = randint(1, 4)
    entity.take_damage(dmg)
    return f"{self.name} attacks a {entity.name} for {dmg} damage."
