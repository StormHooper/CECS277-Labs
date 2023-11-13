from random import choice

from easy_goblin import EasyGoblin
from easy_skeleton import EasySkeleton
from easy_zombie import EasyZombie
from enemy_factory import EnemyFactory


class BeginnerFactory(EnemyFactory):
  def create_random_enemy(self):
    return choice((EasyGoblin(), EasySkeleton(), EasyZombie()))
