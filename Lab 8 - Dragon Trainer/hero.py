from entity import Entity
from random import randint


class Hero(Entity):

  def basic_attack(self, other):
    '''
    basic_attack - hero slashes with their sword rolls 2 D6 having damgage range 2-12.
    '''
    damage = randint(1, 6) + randint(1, 6)
    other.take_damage(damage)
    return f"\nYou slash the {other.name} with your sword for {damage} damage!"

  def special_attack(self, other):
    '''
    special_attack - hero shoots an arrow which does 1-12 damage on single roll.
    '''
    damage = randint(1, 12)
    other.take_damage(damage)
    return f"\nYou shoot the {other.name} with your arrow for {damage} damage!"
