# Name: Tyler Pham and Matthew Samar
# Date: 17 October 2023
# Description: Escape room. The program chooses three out of five doors to be unlocked.
# After every attempt, if the user hasn't unlocked the door, they will get a clue. 
# After unlocking every door, they will be congratulated and the game ends.
from random import choice

from basic_door import BasicDoor
from check_input import get_int_range
from code_door import CodeDoor
from combo_door import ComboDoor
from deadbolt_door import DeadboltDoor
from locked_door import LockedDoor


def open_door(door):
  '''
  Passes door object that user will try to unlock.
  The loop continues until the user has unlocked the door.
  '''
  print(door.examine_door())
  choice = get_int_range(door.menu_options(), 1, door.get_menu_max())
  print(door.attempt(choice))
  while not door.is_unlocked():
    print(door.clue())
    choice = get_int_range(door.menu_options(), 1, door.get_menu_max())
    print(door.attempt(choice))
  print(door.success())


def main():
  '''
  Program begins by setting an empty door list and fills the list with random doors.
  The first for-loop ensures that the solutions are random if the same type is chosen.
  The next loop opens each of the doors in the order they were randomly chosen.
  '''
  print("Welcome to the Escape Room. You must unlock 3 doors to escape...\n")
  doors = []
  for _ in range(3):
    doors_list = [BasicDoor(), LockedDoor(), DeadboltDoor(), ComboDoor(), CodeDoor()]
    doors.append(choice(doors_list))
  for knobs in doors:
    open_door(knobs)
  print("Congratulations! You escaped... this time.")


main()
