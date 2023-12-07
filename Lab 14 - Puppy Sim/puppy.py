from stateasleep import StateAsleep


class Puppy():

  def __init__(self, name):
    self._state = StateAsleep()
    self._feeds = 0
    self._plays = 0
    self._name = name

  @property
  def name(self):
    return self._name

  @property
  def feeds(self):
    return self._feeds

  @property
  def plays(self):
    return self._plays

  def change_state(self, new_state):
    self._state = new_state

  def throw_ball(self):
    return self._state.play(self)

  def give_food(self):
    return self._state.feed(self)

  def inc_feeds(self):
    self._feeds += 1

  def inc_plays(self):
    self._plays += 1

  def reset(self):
    self._plays = 0
    self._feeds = 0
