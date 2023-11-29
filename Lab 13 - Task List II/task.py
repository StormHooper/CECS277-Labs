class Task:
  '''
  description – string description of the task.
  date – due date of the task. A string in the format: MM/DD/YYYY
  time – time the task is due. A string in the format: HH:MM
  '''  
  def __init__(self, description, date, time):
    self._desc = description
    self._date = date
    self._time = time

  @property
  def desc(self):
    return self._desc

  @property
  def date(self):
    return self._date

  @property
  def time(self):
    return self._time


  def __str__(self):
    '''
    returns string used to display task's information to user
    '''
    return f"{self.desc} - Due: {self.date} at {self.time}"


  def __repr__(self):
    '''
    returns string used to write the task to file
    '''
    return f"{self.desc},{self.date},{self.time}"


  def __lt__(self, other):
    '''
    returns true if self task is less than other task.
    Compare by year, then month, then day, then hour, then minute. 
    Then task description by alphabetical order. (Real tiresome)
    '''
    taskDate = [int(i) for i in self.date.split('/')]
    otherDate = [int(i) for i in other.date.split('/')]
    taskTime = [int(i) for i in self.time.split(':')]
    otherTime = [int(i) for i in other.time.split(':')]
    if taskDate[2] != otherDate[2]:
      return taskDate[2] < otherDate[2]
    elif taskDate[0] != otherDate[0]:
      return taskDate[0] < otherDate[0]
    elif taskDate[1] != otherDate[1]:
      return taskDate[1] < otherDate[1]
    elif taskTime[0] != otherTime[0]:
      return taskTime[0] < otherTime[0]
    elif taskTime[1] != otherTime[1]:
      return taskTime[1] < otherTime[1]
    else:
      return self.desc.lower() < other.desc.lower()
