from random import shuffle

from card import Card


class Deck(Card):
  '''
  Attributes:
  _cards - a list of Card objects that are in the deck (4 suits and 13 ranks)
  '''

  def __init__(self):
    self._cards = [Card(suit, rank) for suit in range(4) for rank in range(13)]

  def shuffle(self):
    '''
    Shuffles the deck using the random class that can pass a list.
    '''
    shuffle(self._cards)

  def draw_card(self):
    '''
    Remove the topmost card from deck and return it.
    '''
    return self._cards.pop(0)

  def __len__(self):
    return len(self._cards)
