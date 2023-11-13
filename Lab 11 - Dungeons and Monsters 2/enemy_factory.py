from abc import ABC, abstractmethod


class EnemyFactory(ABC):  
  @abstractmethod
  def create_random_enemy(self):
    pass
    