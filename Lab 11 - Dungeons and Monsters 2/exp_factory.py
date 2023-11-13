from random import choice

from enemy_factory import EnemyFactory
from goblin import Goblin
from skeleton import Skeleton
from zombie import Zombie


class ExpertFactory(EnemyFactory):
  def create_random_enemy(self):
    return choice((Goblin(), Skeleton(), Zombie()))
    