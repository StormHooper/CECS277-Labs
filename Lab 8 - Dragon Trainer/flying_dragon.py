from dragon import Dragon
from random import randint


class FlyingDragon(Dragon):

  def __init__(self, name, max_hp, swoops):
    super().__init__(name, max_hp)
    self.swoops = swoops

  def special_attack(self, other):
    '''
    If flying dragon has swoops, they can deal 5-8 damage to player.
    '''
    if self.swoops > 0:
      damage = randint(5, 8)
      other.take_damage(damage)
      self.swoops -= 1
      return f"{self.name} swoops down and knocks you over for {damage} damage!\n"
    else:
      return f"{self.name} swoops down, misses, and deals no damage!\n"

  def __str__(self):
    return f"{super().__str__()} \nSwoop attacks Remaining: {self.swoops}"
