# Student Name: Cuong Ha (ha000065)

from sudoku import Sudoku

'''
This class represents Depth First Search algorithm which will
be our main algorithm to solve the sudoku games.
'''
class DFS:
  '''
  __init__: algorithm initialization
  Argument(s):
    - initial: the initial state of the game
  Attribute(s):
    - initial_state: the initial state of the game
    - frontier : stack-like list of states ready to be visited
    - num_step: keeps track how many steps it takes to find solution
  '''
  def __init__(self, game):
    self.initial_state = game
    self.frontier = [self.initial_state]
    self.num_steps = 0
    
  '''
  frontier_is_empty: checks if the frontier is empty, if yes then
                     no solution can be found for such sudoku game
  Argument(s):
    - None
  Return:
    - True if length of the frontier is 0
    - False if length of frontier is at least 1
  '''
  def frontier_is_empty(self):
    return len(self.frontier) == 0
  
  '''
  insert_frontier: inserts a state into the beginning of frontier
  Argument(s):
    - state: the state to be added into frontier
  Return:
    - None
  '''
  def insert_frontier(self, state):
    self.frontier.insert(0, state)
  
  '''
  pop_frontier: removes the first state in the frontier
  Argument(s):
    - None
  Return:
    - The first state in the frontier
  '''
  def pop_frontier(self):
    return self.frontier.pop(0)
    
  '''
  solve: essence of the algorithm that looks for the solution
         of a given state
  Argument(s):
    - None
  Return:
    - The solution of the given state if there is one
    - None if there is no solution for the given state
  '''
  def solve(self):
    while True:
      self.num_steps += 1
      if self.frontier_is_empty():
        print("No solution is found. Number of steps taken: " + str(self.num_steps))
        return None
      visiting_state = self.pop_frontier()
      if visiting_state.is_solution():
        print("Solution is found. Number of steps taken: " + str(self.num_steps))
        return visiting_state
      consequential_states = visiting_state.expand()
      if len(consequential_states) > 0:
        for state in consequential_states:
          if state not in self.frontier:
            self.insert_frontier(state)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
