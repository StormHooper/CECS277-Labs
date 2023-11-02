# Name: Tyler Pham and Matthew Samar
# Date: 3 November 2023
# Description: Dungeons and Monsters. A DnD-inspired game.

from random import choice

from check_input import get_int_range
from enemy import Enemy
from hero import Hero
from map import Map


def main():
  player = Hero(input("What is your name, traveler? "))
  dungeon = Map()
  while player.hp:
    dungeon.reveal(player.loc)
    print(f"{player}\n{dungeon.show_map(player.loc)}\n")
    print("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit")
    '''
    User makes a movement choice, in which move will determine what action will happen next.
    '''
    user_choice = get_int_range("Enter choice: ", 1, 5)
    if user_choice == 1:
      move = player.go_north()
    elif user_choice == 2:
      move = player.go_south()
    elif user_choice == 3:
      move = player.go_east()
    elif user_choice == 4:
      move = player.go_west()
    else:
      break
    '''
    m -> monster encounter; i -> healing; n, s -> no action occurs; o -> Invalid move;
    f -> finish
    '''
    if move == "m":
      monster = Enemy()
      print(f"You encounter a {monster}")
      while monster.hp and player.hp:
        print(f"1. Attack {monster.name}\n2. Run Away")
        user_choice = get_int_range("Enter choice: ", 1, 2)
        if user_choice == 1:
          print(player.attack(monster))
          if monster.hp:
            print(monster.attack(player))
        else:
          dungeon.reveal(player.loc)
          print("You ran away!")
          run_choice = "m"
          while run_choice == "o" or run_choice == "m":
            run_choice = choice((player.go_north(), player.go_south(), player.go_east(), player.go_west()))
          break
      if not monster.hp:
        dungeon.remove_at_loc(player.loc)
        print(f"You have slain a {monster.name}\n")        
    elif move == "i":
      if player.hp < player.max_hp:
        player.heal()
        dungeon.remove_at_loc(player.loc)
        print("You found a Health Potion! You drink it to restore your health.\n")
      else:
        print("You are at full health. You decide to save the potion for later.\n")
    elif move == "n":
      print("There is nothing here...\n")
    elif move == "s":
      print("You headed back to the start of the dungeon.\n")
    elif move == "o":
      print("You cannot go that way...\n")
    else:
      print("Congratulations! You found the exit.")
      break
  '''
  Game over if player dies or finds the exit.
  '''
  if not player.hp:
    print("You died.")
  print("Game Over")

main()
