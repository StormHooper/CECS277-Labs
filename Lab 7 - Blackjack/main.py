# Name: Tyler Pham and Matthew Samar
# Date: 10 October 2023
# Description: Blackjack. Player plays against the program (dealer) in blackjack.
# Both player and dealer draw cards, the one with most points without busting wins.
from check_input import get_int_range, get_yes_no
from dealer import Dealer
from deck import Deck
from player import Player


def display_winner(pScore, dScore, points):
  '''
  Displays winner of the round based on player and dealer hand scores.
  '''
  if (pScore < dScore and dScore < 22) or (dScore < 22 and pScore >= 22):
    print("\nDealer wins.")
    points[1] += 1
  elif (dScore < pScore and pScore < 22) or (pScore < 22 and dScore >= 22):
    print("\nPlayer wins.")
    points[0] += 1
  else:
    print("\nTie.")
  print(f"Player's points: {points[0]}\nDealer's points: {points[1]}")


def main():
  print("-Blackjack-")
  deck = Deck()
  deck.shuffle()
  points_list = [0, 0]
  play = True
  while play:
    '''
    Reshuffles the deck if its size is less than 15. Sets player's hand for this turn.
    '''
    if len(deck) < 15:
      deck = Deck()
      deck.shuffle()
    player_hand = Player(deck)
    '''
    Start of the player's turn. Loop will end if player busts are enters '2' to stay.
    '''
    while True:
      print(f"\nPlayer's Cards:\n{player_hand}")
      if player_hand.score() >= 22:
        print("Bust!")
        break
      choice = get_int_range("1. Hit \n2. Stay \nEnter choice: ", 1, 2)
      if choice == 1:
        player_hand.hit()
      else:
        break
    '''
    The dealer's hand is set and plays their turn.
    '''
    dealer_hand = Dealer(deck)
    dealer_hand.play()
    '''
    Display the winner and ask to play again.
    '''
    display_winner(player_hand.score(), dealer_hand.score(), points_list)
    play = get_yes_no("Play again? (Y/N): ")


main()
