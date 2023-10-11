from dragon import Dragon
from random import randint


class FireDragon(Dragon):

  def __init__(self, name, max_hp, f_shots):
    super().__init__(name, max_hp)
    self.f_shots = f_shots

  def special_attack(self, other):
    '''
    If fire dragon has any shots left, they can deal 5-9 damage to player.
    '''
    if self.f_shots > 0:
      damage = randint(5, 9)
      other.take_damage(damage)
      self.f_shots -= 1
      return f"{self.name} engulfs you in flames for {damage} damage!\n"
    else:
      return f"{self.name} puffs a small cloud of smoke that deals no damage!\n"

  def __str__(self):
    return f"{super().__str__()} \nFire Shots Remaining: {self.f_shots}"
