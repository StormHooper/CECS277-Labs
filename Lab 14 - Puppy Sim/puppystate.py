from abc import ABC, abstractmethod


class PuppyState(ABC):
  @abstractmethod
  def feed(self, puppy):
    pass

  @abstractmethod
  def play(self, puppy):
    pass
    