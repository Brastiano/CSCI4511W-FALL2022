# Student Name: Cuong Ha

import copy

'''
This is a class for sudoku puzzle. More specifically,
the instances of this class are the states of the game.
From the initial board, we can derive multiple consequential
boards just by filling in one of the empty squares on the
current board.
Ex:  | 0 1 2 3 4 5 6 7 8
   ---------------------
   0 | 0 0 0 0 0 0 0 0 0
   1 | 0 0 0 0 0 0 0 0 0
   2 | 0 0 0 0 0 0 0 0 0
   3 | 0 0 0 0 0 0 0 0 0
   4 | 0 0 0 0 0 0 0 0 0
   5 | 0 0 0 0 0 0 0 0 0
   6 | 0 0 0 0 0 0 0 0 0
   7 | 0 0 0 0 0 0 0 0 0
   8 | 0 0 0 0 0 0 0 0 0
'''
class Sudoku:
  '''
  __init__: game initialization
  Argument(s):
    - board: a list of lists representing the game's board (as shown)
      Ex: [ [0, 9, 6, 4, 5, 0, 0, 0, 0],
            [0, 8, 4, 0, 0, 1, 7, 0, 9],
            [0, 0, 0, 8, 0, 0, 0, 5, 1],
            [4, 2, 5, 0, 6, 0, 0, 0, 0],
            [0, 0, 7, 5, 0, 9, 2, 0, 0],
            [0, 0, 0, 0, 3, 0, 6, 7, 5],
            [7, 5, 0, 0, 0, 2, 0, 0, 0],
            [2, 0, 9, 1, 0, 0, 5, 4, 0],
            [0, 0, 0, 0, 7, 5, 1, 2, 0]  ]
  Attribute(s):
    - board: a list of lists representing the game's board
    - rows: number of rows on the board
    - columns: number of columns on the board
  '''
  def __init__(self, game_board, rows = 9, columns = 9):
    self.board = game_board
    self.rows = rows
    self.columns = columns
    
  '''
  __eq__: checks if two sudoku instances are the same
  Argument(s):
    - other: the game instance used to compare with this one
  Return:
    - True if two instances are the same
    - False if at least one attribute of one instance is different
      than the other's
  '''
  def __eq__(self, other):
    return self.board == other.board and self.rows == other.rows and self.columns == other.columns
  
  '''
  __str__: prints the sudoku board in a proper form
  Argument(s):
    - None
  Return:
    - An easy-to-visualize form of sudoku board
  '''
  def __str__(self):
    sudoku_board = ""
    for row in range (self.rows):
      if row == 3 or row == 6:
        sudoku_board += "---------------------\n"
      for column in range (self.columns - 1):
        if column == 3 or column == 6:
          sudoku_board += "| "
        sudoku_board += str(self.board[row][column])
        sudoku_board += " "
      sudoku_board += str(self.board[row][self.columns - 1])
      sudoku_board += "\n"
    return sudoku_board  
    
  '''
  is_valid: checks if the given number exists in a row,
            a column or a sub-square (as shown) yet
  Ex: 0 0 0 | 0 0 0 | 0 0 0
      0 0 0 | 0 0 0 | 0 0 0
      0 0 0 | 0 0 0 | 0 0 0
      ---------------------
      0 0 0 | 0 0 0 | 0 0 0
      0 0 0 | 0 0 0 | 0 0 0
      0 0 0 | 0 0 0 | 0 0 0
      ---------------------
      0 0 0 | 0 0 0 | 0 0 0
      0 0 0 | 0 0 0 | 0 0 0
      0 0 0 | 0 0 0 | 0 0 0
  Argument(s):
    - row: the row the number is in
    - column: the column the number is in
    - num: the number whose location is being determined
  Return:
    - True if the number exists in either row, column or sub-square
    - False if the number doesn't exist in row, column and sub-square
  '''
  def exist(self, row, column, num):
    # Check if the number appears in the given row
    for column_ in range (self.columns):
      if self.board[row][column_] == num:
        return True;
    # Check if the number appears in the given column
    for row_ in range (self.rows):
      if self.board[row_][column] == num:
        return True;
    # Check if the number appears in the square it is in
    # This tuple is the location of the first square of the sub-square
    start = (-1,-1)
    if (0 <= row <= 2 and 0 <= column <= 2): start = (0,0)
    elif (0 <= row <= 2 and 3 <= column <= 5): start = (0,3)
    elif (0 <= row <= 2 and 6 <= column <= 8): start = (0,6)
    elif (3 <= row <= 5 and 0 <= column <= 2): start = (3,0)
    elif (3 <= row <= 5 and 3 <= column <= 5): start = (3,3)
    elif (3 <= row <= 5 and 6 <= column <= 8): start = (3,6)
    elif (6 <= row <= 8 and 0 <= column <= 2): start = (6,0)
    elif (6 <= row <= 8 and 3 <= column <= 5): start = (6,3)
    elif (6 <= row <= 8 and 6 <= column <= 8): start = (6,6)
    for x in range (start[0], start[0] + 3):
      for y in range (start[1], start[1] + 3):
        if self.board[x][y] == num:
          return True
    return False
  
  '''
  find_empty: finds a square that is not yet filled (has 0 as value)
  Argument(s):
    - None
  Return:
    - Location of a first encountered empty square if there is one
    - If there is no empty square, return None
  '''
  def find_empty(self):
    for row in range (self.rows):
      for column in range (self.columns):
        if self.board[row][column] == 0:
          return row, column
    return None
    
  '''
  expand: finds a list of resulting boards from filling a number to one empty
          position on the current board
  Argument(s):
    - None
  Return:
    - A list of boards that is resulted from the current board
  '''
  def expand(self):
    # List containing all the resulting boards, empty at first
    children = []
    # Get the location of an empty square
    row, column = self.find_empty()
    # Try to fill every number from 1 to 9 into the empty square
    for num in range (1,10):
      if not self.exist(row, column, num):
        child_board = copy.deepcopy(self.board)
        child_board[row][column] = num
        children.append(Sudoku(game_board = child_board))
    return children
    
  '''
  is_solution: checks if every square of current sudoku board is filled, in
               other words, check if current sudoku board can have any more
               resulting boards
  Argument(s):
    - None
  Return:
    - True if there is no empty square left on the board to fill
    - False if there is at least one square left on the board to fill
  '''
  def is_solution(self):
    for row in range (self.rows):
      for column in range (self.columns):
        if self.board[row][column] == 0: return False
    return True
