from abc import ABC, abstractmethod


class Door(ABC):

  @abstractmethod
  def examine_door(self):
    pass

  @abstractmethod
  def menu_options(self):
    pass

  @abstractmethod
  def get_menu_max(self):
    pass

  @abstractmethod
  def attempt(self, option):
    pass

  @abstractmethod
  def is_unlocked(self):
    pass

  @abstractmethod
  def clue(self):
    pass

  @abstractmethod
  def success(self):
    pass
