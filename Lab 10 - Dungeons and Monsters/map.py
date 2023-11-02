class Map:
  _instance = None
  _initialized = False
  
  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    if not Map._initialized:
      with open("map.txt", "r") as f:
        self._map = [list(row) for row in f.readlines()]
      self._revealed = [[False for _ in row] for row in self._map]
      Map._initialized = True

  def __getitem__(self, row):
    return self._map[row]

  def __len__(self):
    '''
    Return the number of rows in the map list.
    '''
    return len(self._map)

  def show_map(self, loc):
    '''
    Return map as string in 5x5 matrx of characters. 
    Unrevealed -> 'x', hero's location -> '*'.
    '''
    mapped = [[self[i][j] if self._revealed[i][j] or self[i][j] == "\n"
               else "x" for j in range(len(self[i]))] for i in range(len(self))]
    mapped[loc[0]][loc[1]] = "*"
    return "".join([" ".join(row) for row in mapped])

  def reveal(self, loc):
    '''
    Sets value in 2D revealed list at the specified location to True.
    '''
    self._revealed[loc[0]][loc[1]] = True

  def remove_at_loc(self, loc):
    '''
    Overwrites the character in the map list at the specified location with 'n'.
    '''
    self[loc[0]][loc[1]] = "n"
  