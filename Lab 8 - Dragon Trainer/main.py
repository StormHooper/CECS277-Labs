# Name: Tyler Pham and Matthew Samar
# Date: 13 October 2023
# Description: Dragon Trainer. A game where the player fights against 3 dragons.
# After the player types their name, they can choose a target to slash or shoot.
from check_input import get_int_range
from dragon import Dragon
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
from hero import Hero
from random import randint


def main():
  '''
  Set up the Player, welcome them, and set the Dragons
  '''
  player = Hero(input("What is your name, challenger? "), 50)
  print(f"Welcome to dragon training, {player.name}.\n"
  "You must defeat 3 dragons.\n")
  dragons = [
      Dragon("Garchomp", 25),
      FireDragon("Charizard", 20, 2),
      FlyingDragon("Salamence", 15, 5)
  ]
  '''
  Enter the loop that ends if all dragons or the player is defeated.
  '''
  training = True
  while training:
    '''
    Prints the player, their hp, and targets. Then gets weapon choice.
    '''
    print(player)
    for d in range(len(dragons)):
      print(f"{d+1}. Attack {dragons[d]}")
    target = get_int_range("Choose a dragon to attack: ", 1, len(dragons))
    print("\nAttack with: \n1. Sword (2 D6) \n2. Arrow (1 D12)")
    weapon = get_int_range("Enter Weapon: ", 1, 2)
    '''    
    Print attack with correct weapon and the damage done to dragon.
    If a dragon is defeated, that will be printed.
    '''
    if weapon == 1:
      print(player.basic_attack(dragons[target - 1]))
    else:
      print(player.special_attack(dragons[target - 1]))
    if dragons[target - 1].hp <= 0:
      print(f"You have defeated the {dragons[target-1].name}!")
      dragons.pop(target - 1)
    '''
    If the player has defeated all dragons, congratulate the player.
    Otherwise, the dragons will attack at random.
    '''
    if len(dragons) == 0:
      print("\nCongratulations! You have defeated all 3 dragons, "
      "you have passed the trials.")
      training = False
    else:
      dragon_attack = randint(1, 2)
      if dragon_attack == 1:
        print(dragons[randint(0, len(dragons) - 1)].basic_attack(player))
      else:
        print(dragons[randint(0, len(dragons) - 1)].special_attack(player))
    '''
    If the player has no heath points after dragon attacks, then the game ends.
    '''
    if player.hp == 0:
      print("You have been defeated by the dragons! \n"
      "Take time to recover then attempt the trials again.")
      training = False


main()
