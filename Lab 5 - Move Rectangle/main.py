# Name: Tyler Pham and Matthew Samar
# Date: 22 September 2023
# Description: Move Rectangle. Player decides size of rectangle (limit maximum 5x5).
# The rectangle is then displayed at the origin of a 20x20 grid.
# The player can move the rectangle about the grid but not off it.
import check_input
import rectangle


def display_grid(grid):
  '''
  Pass in the grid and display the contents of the grid.
  '''
  for row in grid:
    for column in row:
      print(column, end=" ")
    print()


def reset_grid(grid):
  '''
  Pass in the grid and overwrite the contents with all ‘.’s.
  '''
  grid[:] = [['.' for column in range(20)] for row in range(20)]


def place_rect(grid, rect):
  '''
  Pass in the grid and the rectangle. At the location of  
  the rectangle (x, y) on the grid, overwrite the ‘.’ characters 
  with ‘*’s using the width and height of the rectangle.
  '''
  x, y = rect.get_coords()
  w, h = rect.get_dimentions()
  for i in range(h):
    for j in range(w):
      grid[y+i][x+j] = "*"


def main():
  '''
  Game start. Sets the rectangle and grid up for initial play.
  '''
  print("-Rectangle-")
  wide = check_input.get_int_range("Enter rectangle width (1-5): ", 1, 5)
  tall = check_input.get_int_range("Enter rectangle height (1-5): ", 1, 5)
  box = rectangle.Rectangle(wide, tall)
  grid = [[]]
  play = True
  '''
  Displays the grid and rectangle, then asks for direction to move rectangle.
  The loop continues until the user types '5' as their choice.
  '''
  while play:
    reset_grid(grid)
    place_rect(grid, box)
    display_grid(grid)
    
    movable = False   
    while not movable:
      choice = check_input.get_int_range(
          "Enter Direction: \n1. Up \n2. Down \n"
          "3. Left \n4. Right \n5. Quit \n", 1, 5)
  
      if choice == 1 and box.y > 0:
        box.move_up()
        movable = True
      elif choice == 2 and (box.y + box.height) < len(grid):
        box.move_down()
        movable = True
      elif choice == 3 and box.x > 0:
        box.move_left()
        movable = True
      elif choice == 4 and (box.x + box.width) < len(grid[0]):
        box.move_right()
        movable = True
      elif choice == 5:
        play = False
        movable = True
      else:
        print("Unable to move there.")


main()
