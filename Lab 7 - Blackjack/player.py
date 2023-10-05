class Player:
  '''
  Attributes:
  _deck - reference to deck of cards that both player and dealer use.
  _hand - list of Cards that player is currently holding.
  '''

  def __init__(self, deck):
    self._hand = sorted([deck.draw_card(), deck.draw_card()])
    self._deck = deck

  def hit(self):
    '''
    Adds another card from deck to player's hand and resorts them.
    '''
    self._hand.append(self._deck.draw_card())
    self._hand.sort()

  def score(self):
    '''
    Totals up cards in player's hand and returns that score.
    '''
    total = 0
    for card in self._hand:
      if card.rank == "Ace":
        if total <= 10:
          total += 11
        else:
          total += 1
      elif card.rank == "King" or card.rank == "Queen" or card.rank == "Jack":
        total += 10
      else:
        total += int(card.rank)
    return total

  def __str__(self):
    return '\n'.join(str(card) for card in self._hand) + f"\nScore: {self.score()}"
