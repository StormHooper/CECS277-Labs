# Name: Tyler Pham and Matthew Samar
# Date: 5 september 2023
# Description: Ship, Captain, and Crew. Two players will take turns rolling five dice.
# They want to roll [6, 5, 4] in this order to get cargo points with the last two dice
# the player with the most cargo points wins. 
import random

import check_input


def roll_dice(dice):
  '''
  Pass list of dice. Randomize values of each dice 1-6. Sort values in descending order.
  '''
  for i in range(0, len(dice)):
    rolled_value = random.randint(1,6)
    dice[i] = rolled_value
  dice.sort(reverse=True)


def display_dice(name, dice):
  '''
  Pass name of list, list of dice. Display dice values separated by spaces.
  '''
  print(name, end=" = ")
  for i in range(len(dice)):
    print(dice[i], end=" ")
  print()


def find_winner(player_points):
  '''
  Pass two player's points as list. Display points and winner. If tie, display tie.
  '''
  print("\nScore:")
  print(f"Player #1: {player_points[0]}")
  print(f"Player #2: {player_points[1]}")
  
  if player_points[0] > player_points[1]:
    print("Player #1 won!")
  elif player_points[1] > player_points[0]:
    print("Player #2 won!")
  elif player_points[1] == player_points[0] == 0:
    print("Arr! Looks like we have a pair of landlubbers with us!")
  else:
    print("Avast, ye lads! We have a tie!")
    

def main():
  print("- Ship, Captain, and Crew! –")
  cargo_scores = [0,0]
  '''
  Defined variables at beginning of for loop to reset values for each player. 
  Variable 'scc' stands for 'Ship Captain Crew'.
  '''
  for player in range(1,3):
    keeps = []
    roll = [0,0,0,0,0]
    scc = [6,5,4]
    turns = 3
    roll_again = True

    print(f"\nPlayer #{player} Turn:")
    '''
    Start of player rolling.
    '''
    while turns != 0 and roll_again is True:
      roll_dice(roll)
      display_dice("Roll", roll)
      '''
      Checks rolls for 6, 5, 4 and removes die.
      '''
      for i, keep in enumerate(scc):
        if keep in roll and len(keeps) == i:
          keeps.append(keep)
          roll.remove(keep)
          if keep == 6:
            print("Yo ho ho! Ye secured a ship!")
          elif keep == 5:
            print("Shiver me timbers! A Capt'n!")
          else:
            print("Ye bribed a crew with Grog!")
      '''
      Decrease turn. Displays the keeps list and cargo sums if keep is complete.
      '''
      display_dice("Keep", keeps)
      turns -= 1
      sum = 0
      if keeps == scc:
        display_dice("Cargo", roll)
        for i in range(len(roll)):
          sum += roll[i]
        if turns > 0:
          print(f"Your cargo points are: {sum}")
      cargo_scores[player-1] = sum
      '''
      Asks user if they want to roll again if their turn is not over.
      '''  
      if turns != 0:
        roll_again = check_input.get_yes_no("\nRoll again? ")
    '''
    Displays the player's final points at the end of their turn.
    '''
    print(f"Player #{player} points = {cargo_scores[player-1]}")

  '''
  Displays the winner at the end of the game after both turns.
  '''
  find_winner(cargo_scores)


main()
