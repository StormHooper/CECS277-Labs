import stateeat
from puppystate import PuppyState


class StateAsleep(PuppyState):
  def feed(self, puppy):
    puppy.change_state(stateeat.StateEat())
    return f"{puppy.name} wakes up and comes running to eat."

  def play(self, puppy):
    return f"{puppy.name} is asleep. It doesn't want to play right now."
