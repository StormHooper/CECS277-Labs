from random import randint

import stateasleep
from puppystate import PuppyState
from stateplay import StatePlay


class StateEat(PuppyState):

  def feed(self, puppy):
    appetite = randint(2,3)
    if puppy.feeds >= appetite:
      puppy.reset()
      puppy.change_state(stateasleep.StateAsleep())
      return f"{puppy.name} is full and falls asleep."
    else:
      puppy.inc_feeds()
      return f"{puppy.name} continues to eat as you add another scoop of kibble to its bowl."

  def play(self, puppy):
    puppy.reset()
    puppy.change_state(StatePlay())
    return f"{puppy.name} ignores the food to after the ball."
