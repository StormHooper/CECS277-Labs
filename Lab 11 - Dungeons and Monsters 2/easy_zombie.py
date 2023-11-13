from random import randint

from entity import Entity


class EasyZombie(Entity):
  def __init__(self):
    super().__init__("Zombie", randint(4,5))

  def attack(self, entity):
    dmg = randint(1, 5)
    entity.take_damage(dmg)
    return f"{self.name} attacks a {entity.name} for {dmg} damage."
