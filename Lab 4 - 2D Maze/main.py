# Name: Tyler Pham and Matthew Samar
# Date: 15 September 2023
# Description: 2D Maze. The player is tasked with solving a maze read from a file. 
# The player can move north, south, east, west but not through '*'. 
import check_input


def read_maze():
  '''
  Reads file content and store in 2D list. Each character store in seperate element.
  Return filled 2D list.
  '''
  maze_list = []
  with open("maze.txt", "r") as file:
    for line in file:
      maze_list.append(list(line.strip()))
  return maze_list


def find_start(maze):
  '''
  Pass filled maze. Search through elements for 's' using nested loops.
  Return location as two item 1D list with first item in row, and second in column.
  '''
  loc  = [0,0]
  for row in range(len(maze)):
    for column in range(len(maze[row])):
      if maze[row][column] == 's':
        loc  = [row, column]
  return loc


def display_maze(maze, loc):
  '''
  Pass filled maze and user's location. Iterate through contents of maze. 
  Display each character in maze in matrix format. 
  Display 'X' on user's location but do not put into 2D list.
  '''
  for row in range(len(maze)):
    for column in range(len(maze[row])):
      if row == loc[0] and column == loc[1]:
        print('X', end = "")
      else:
        print(maze[row][column], end = "")
    print()


def main():
  '''
  Game start. Reads maze file and sets up necessary variables.
  '''
  print("-Maze Solver-")
  maze = read_maze()
  solved = False
  x_loc = find_start(maze)
  '''
  Find the ending location of the maze. Similar logic to find_start().
  '''
  finish_loc = [0,0]
  for row in range(len(maze)):
    for column in range(len(maze[row])):
      if maze[row][column] == 'f':
        finish_loc = [row, column]
  '''
  Display the maze and movement options.
  '''
  display_maze(maze,x_loc)
  while not solved:
    movable = False
    movement = [0,0]
    while not movable:
      print("1. Go North \n2. Go South \n3. Go East \n4. Go West")
      move = check_input.get_int_range("Enter Choice: ", 1, 4)
      if move == 1:
        movement[0] = -1
      elif move == 2:
        movement[0] = 1
      elif move == 3:
        movement[1] = 1
      elif move == 4:
        movement[1] = -1
      '''
      After user makes movement option, program processes its validity.
      '''
      if maze[x_loc[0]+movement[0]][x_loc[1]+movement[1]] == '*':
        print("You cannot move there.")
        movement = [0,0]
      else:
        movable = True
    '''
    Updates player's position in the maze.
    '''
    x_loc[0] += movement[0]
    x_loc[1] += movement[1]
    display_maze(maze,x_loc)
    '''
    If the player is on the finish, 'solved' is set to true and game ends.
    '''
    if x_loc == finish_loc:
      solved = True
  print("Congratulations! You solved the maze.")
      

main()