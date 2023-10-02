from task import Task


class Tasklist:
  '''
  tasklist - a list of Task objects
  '''
  def __init__(self):
    with open("tasklist.txt", "r") as file:
      file_list = [[i for i in task.replace('\n', '').split(',')] 
                   for task in file.readlines()]
    self.tasklist = sorted([Task(task[0], task[1], task[2]) for task in file_list])

  
  def add_task(self, desc, date, time):
    '''
    Construct new task using parameters, append to tasklist, then sort.
    '''
    self.tasklist.append(Task(desc, date, time))
    self.tasklist.sort()
    

  def mark_complete(self):
    '''
    Remove the current task from tasklist.
    '''
    self.tasklist.pop(0)
    

  def save_file(self):
    '''
    Write contents of tasklist back to file using Task's __repr__ method
    Description, date, and time separated by commas.
    '''
    with open("tasklist.txt", 'w') as file:
      file.write('\n'.join([repr(task) for task in self.tasklist]))
    

  def __getitem__(self, index):
    '''
    return Task from list at specified index.
    '''
    return self.tasklist[index]
    

  def __len__(self):
    '''
    return number of items in tasklist
    '''
    return len(self.tasklist)
