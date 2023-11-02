from abc import ABC, abstractmethod


class Entity(ABC):

  def __init__(self, name, max_hp):
    self._name = name
    self._hp = max_hp
    self._max_hp = max_hp

  @property
  def name(self):
    return self._name

  @property
  def hp(self):
    return self._hp

  def take_damage(self, dmg):
    self._hp -= dmg
    if self._hp <= 0:
      self._hp = 0

  def heal(self):
    self._hp = self._max_hp

  def __str__(self):
    return f"{self.name}\nHP: {self.hp}/{self._max_hp}"

  @abstractmethod
  def attack(self, entity):
    pass
