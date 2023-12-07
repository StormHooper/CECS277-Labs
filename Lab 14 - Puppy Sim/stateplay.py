from random import randint

import stateasleep
from puppystate import PuppyState


class StatePlay(PuppyState):

    def feed(self, puppy):
      return f"{puppy.name} ignores the food and keeps wanting to play."

    def play(self, puppy):
      energy = randint(2,3)
      if puppy.plays >= energy:
        puppy.reset()
        puppy.change_state(stateasleep.StateAsleep())
        return f"{puppy.name} is tired from playing and falls asleep."
      else:
        puppy.inc_plays()
        return f"{puppy.name} is a very competitive puppy and keeps chasing the ball."
