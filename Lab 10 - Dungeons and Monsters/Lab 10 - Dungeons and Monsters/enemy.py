from random import choice, randint

from entity import Entity


class Enemy(Entity):
  def __init__(self):
    super().__init__(choice(("Goblin", "Vampire", "Ghoul", "Skeleton", "Zombie")), 
                     randint(4,8))

  def attack(self, entity):
    dmg = randint(1, 4)
    entity.take_damage(dmg)
    return f"{self.name} attacks a {entity.name} for {dmg} damage."
