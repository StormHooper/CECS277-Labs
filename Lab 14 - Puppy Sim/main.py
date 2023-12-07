# Name: Tyler Pham and Matthew Samar
# Date: 5 December 2023
# Description: Task List II. The program will start with a list read from a file.
# The user can make changes to the list such as marking complete or adding to the list.
# Changes to the list are done by overwriting the text file.


from puppy import Puppy
from check_input import get_int_range


def main():
  puppy = Puppy(input("Congratulations on your new puppy! What is its name?\n"))
  choice  = 0
  while choice != 3:
    choice = get_int_range("What would you like to do?"
      "\n1. Feed the puppy"
      "\n2. Play with the puppy"
      "\n3. Quit"
      "\nEnter Choice: ", 1, 3)
    print()
    if choice == 1:
      print(puppy.give_food())
    elif choice == 2:
      print(puppy.throw_ball())
  print(f"{puppy.name} says Goodbye!")

main()