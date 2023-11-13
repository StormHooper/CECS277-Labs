from random import randint

from entity import Entity


class EasyGoblin(Entity):
  def __init__(self):
    super().__init__("Goblin", randint(4,6))

  def attack(self, entity):
    dmg = randint(2, 5)
    entity.take_damage(dmg)
    return f"{self.name} attacks a {entity.name} for {dmg} damage."
