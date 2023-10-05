from player import Player


class Dealer(Player):
  '''
  Plays a round for the dealer. 
  The dealer hits on scores 16 or lower, and stays on scores 17 or more.
  '''

  def play(self):
    play = True
    while play:
      print("\nDealer's Cards:")
      print(str(self))
      if self.score() < 17:
        print("Dealer Hits!")
        self.hit()
      else:
        play = False
    if self.score() >= 22:
      print("Bust!")
