class Card:
  '''
  Attributes:
  _rank - an integer index 0-12 representing card ranks:
    ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
  _suit - an integer index 0-3, representing card suits: 
    ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  '''

  def __init__(self, suit, rank):
    self._suit = suit
    self._rank = rank

  @property
  def rank(self):
    valid_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 
                   'Jack', 'Queen', 'King', 'Ace']
    return valid_ranks[self._rank]

  def __str__(self):
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    return f"{self.rank} of {suits[self._suit]}"

  def __lt__(self, other):
    return self._rank < other._rank
