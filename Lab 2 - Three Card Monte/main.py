# Name: Tyler Pham and Matthew Samar
# Date: 29 August 2023
# Description: Three Card Monte.
import random

import check_input


def get_users_bet(money):
  '''
  Displays money amount and bet amount. Takes paramenter 'money'. Returns 'bet' variable
  '''
  print(f"\nYou have ${money}.", end=" ")
  bet = check_input.get_int_range("How much you wanna bet? ", 1, money)
  return bet


def get_users_choice():
  '''
  Displays card choices and takes user choice. Returns choice.
  '''
  print("+-----+ +-----+ +-----+")
  print("|     | |     | |     |")
  print("|  1  | |  2  | |  3  |")
  print("|     | |     | |     |")
  print("+-----+ +-----+ +-----+")
  choice = check_input.get_int_range("Find the queen: ", 1, 3)
  return choice


def display_queen_loc(queen_loc):
  '''
  Prints location of the queen. Takes parameter 'queen_loc'. Prints correct loction.
  '''
  if queen_loc == 1:
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print("|  Q  | |  K  | |  K  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")
  elif queen_loc == 2:
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print("|  K  | |  Q  | |  K  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")
  else:
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print("|  K  | |  K  | |  Q  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")


def main():
  '''
  Game begins with starting amount $100. Queen is randomized and take user's bet.
  '''
  bank = 100
  print("-Three Card Monte-\nFind the queen to double your bet!")
  queen = 0
  play = True
  while play:
    queen = random.randint(1, 3)
    amount_bet = get_users_bet(bank)
    '''
    User makes a guess. After guessing, queen is displayed.
    '''
    selection = get_users_choice()
    display_queen_loc(queen)
    '''
    Game decides if the user made the correct guess and changes bank amount accordingly.
    '''
    if selection == queen:
      print(f"You got lucky this time! You earned ${amount_bet}!")
      bank += amount_bet
    else:
      print("Sorry, you lose.")
      bank -= amount_bet
      if bank <= 0:
        print("You're out of money. Beat it loser!")
        play = False
    '''
    User may choose to end the game, or keep playing. 
    '''
    if play:
      play = check_input.get_yes_no("Play again? (Y/N): ")
  '''
  End of the game, displaying the final amount user ends up with.
  '''
  print(f"Thanks for playing! You ended with ${bank}")


main()
