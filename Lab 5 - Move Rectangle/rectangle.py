class Rectangle:
  """Representation of a rectangle on the coordinate plane.
  Attributes:
    x (int) - x coord of rectangle
    y (int) - y coord of rectangle
    width (int) - width of rectangle
    height (int) - height of rectangle
  """
  
  def __init__(self, w=1, h=1):
    self.x = 0
    self.y = 0
    self.width = w
    self.height = h

  def get_coords(self):
    '''
    returns the x and y values as a pair
    '''
    return (self.x, self.y)

  def get_dimentions(self):
    """
    returns the rectangle's width and height as a pair
    """
    return (self.width, self.height)

  def move_up(self):
    '''
    moves the rectangle up one row
    '''
    self.y -= 1
  
  def move_down(self):
    '''
    moves the rectangle down one row
    '''
    self.y += 1
  
  def move_left(self):
    '''
    moves the rectangle left one column
    '''
    self.x -= 1
  
  def move_right(self):
    '''
    moves the rectangle right one column
    '''
    self.x += 1
  