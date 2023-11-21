from abc import ABC, abstractmethod


class Plate(ABC):

  @abstractmethod
  def description(self):
    pass

  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def weight(self):
    pass

  @abstractmethod
  def count(self):
    pass
