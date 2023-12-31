# Name: Tyler Pham and Matthew Samar
# Date: 28 November 2023
# Description: Task List II. The program will start with a list read from a file.
# The user can make changes to the list such as marking complete or adding to the list.
# Changes to the list are done by overwriting the text file.
from check_input import get_int_range
from tasklist import Tasklist


def main_menu():
  '''
  displays the main menu and returns user's valid input.
  '''
  print("1. Display current task\n"
        "2. Display all tasks\n"
        "3. Mark current task complete\n"
        "4. Add new task\n"
        "5. Search by date\n"
        "6. Save and quit")
  return get_int_range("Enter a choice: ", 1, 6)


def get_date():
  '''
  Prompts enter year, month, day. Valid years are 2000-3000, months 1-12, days 1-31.
  Adds a 0 if the month or day are only 1 digit long.
  Return date in format MM/DD/YYYY as a string.
  '''
  print("Enter due date:")
  month = str(get_int_range("Enter month: ", 1, 12))
  if len(month) == 1:
    month = f"0{month}"  
  day = str(get_int_range("Enter day: ", 1, 31))
  year = str(get_int_range("Enter year: ", 2000, 3000))

  if len(month) == 1:
    month = f"0{month}"
  if len(day) == 1:
    day = f"0{day}"  

  return f"{month}/{day}/{year}"


def get_time():
  '''
  Prompt enter hour and minute (military time). Valid hours 0-23 and valid minutes 0-59.
  Adds a 0 if the hour or minute are only 1 digit long.
  Return date in form HH:MM. 
  '''
  print("Enter time:")
  hour = str(get_int_range("Enter hour: ", 0, 23))
  minute = str(get_int_range("Enter minute: ", 0, 59))

  if len(hour) == 1:
    hour = f"0{hour}"
  if len(minute) == 1:
    minute = f"0{minute}"

  return f"{hour}:{minute}"


def main():
  play = True
  list = Tasklist()
  '''
  Enter the loop, does not exit until user saves list and quit.
  '''
  while play:
    print(f"-Tasklist-\nTasks to complete: {len(list)}")
    choice = main_menu()
    '''
    After getting user's choice, program processes chosen function.
    '''
    if choice == 1:
      if len(list):
        print(f"Current task is:\n{list.get_current_task()}")
      else:
        print("All tasks are complete!")
    elif choice == 2:
      print("Tasks:")
      [print(f"{i+1}. {task}") for i, task in enumerate(list)]
    elif choice == 3:
      if len(list) >= 1:
        print(f"Marking current task as complete: {list.mark_complete()}")
        if len(list) > 0:
          print(f"New current task is: {list.get_current_task()}")
        else:
          print("No new current tasks")
      else:
        print("No more tasks to complete!")
    elif choice == 4:
      list.add_task(input("Enter a task: "), get_date(), get_time())
    elif choice == 5:
      date_search = get_date()
      print(f"Tasks due on {date_search}:")
      tasks = [t for t in list if t.date == date_search]
      if not tasks:
        print(f"No tasks due on {date_search}")
      else:
        [print(f"{i+1}. {t}") for i, t in enumerate(tasks)]
    else:
      print("Saving List...")
      list.save_file()
      play = False
    '''
    Print new line for next iteration of loop.
    '''
    print()


main()