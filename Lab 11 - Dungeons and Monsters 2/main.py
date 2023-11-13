# Name: Tyler Pham and Matthew Samar
# Date: 10 November 2023
# Description: Dungeons and Monsters 2. Player starts in the top-left corner of the map, 
# where they will be prompted to pick a direction to move. Depending on the space they 
# land on, they will fight monsters, heal, or nothing may happen. 

from random import choice

from beg_factory import BeginnerFactory
from check_input import get_int_range
from exp_factory import ExpertFactory
from hero import Hero
from map import Map


def main():
  player = Hero(input("What is your name, traveler? "))
  diff_choice = get_int_range("Difficulty:\n1. Beginner\n2. Expert\n", 1, 2)
  monster_factory = BeginnerFactory() if diff_choice == 1 else ExpertFactory()
  dungeon = Map()
  map_num = 1
  while player.hp:
    dungeon.reveal(player.loc)
    print(f"{player}\n{dungeon.show_map(player.loc)}\n")
    print("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit")
    '''
    User makes a movement choice, in which move will determine what action will happen next.
    '''
    direction_choice = get_int_range("Enter choice: ", 1, 5)
    if direction_choice == 1:
      move = player.go_north()
    elif direction_choice == 2:
      move = player.go_south()
    elif direction_choice == 3:
      move = player.go_east()
    elif direction_choice == 4:
      move = player.go_west()
    else:
      break
    '''
    m -> monster encounter; i -> healing; n, s -> no action occurs; o -> Invalid move;
    f -> finish
    '''
    if move == "m":
      monster = monster_factory.create_random_enemy()
      print(f"You encounter a {monster}")
      while monster.hp and player.hp:
        print(f"1. Attack {monster.name}\n2. Run Away")
        user_choice = get_int_range("Enter choice: ", 1, 2)
        if user_choice == 1:
          print(player.attack(monster))
          if monster.hp:
            print(monster.attack(player))
        else:
          print("You ran away!")
          dungeon.reveal(player.loc)
          while choice([player.go_north, player.go_south, player.go_east, player.go_west])() == "o":
            continue
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
    elif move == "f":
      if map_num >= 3:
        map_num = 0
      map_num += 1
      dungeon.load_map(map_num)
      print("Congratulations! You found the stairs to the next floor of the dungeon.")
    else:
      print("Hmm... something went wrong here. You're not supposed to see this.")
  '''
  Game over if player dies or finds the exit.
  '''
  if not player.hp:
    print("You died.")
  print("Game Over")

main()
