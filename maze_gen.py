import random

class Maze:
  def __init__(self, size):
    self.size = size

    def make_grid(size):
      line = []
      grid = []
      for i in range(size):
        line.append('#')
      for i in range(size):
        grid.append(list(line))
      return grid

    self.grid = make_grid(self.size)

    def add_new_walls(x, y):
      max = self.size
      new_walls = []
      if x - 1 > 0 and y - 1 > 0:
        new_walls.append([x - 1, y - 1])
      if x - 1 > 0 and y + 1 < max - 1:
        new_walls.append([x - 1, y + 1])
      if x + 1 < max - 1 and y + 1 < max - 1:
        new_walls.append([x + 1, y + 1])
      if x + 1 < max - 1 and y - 1 > 0:
        new_walls.append([x + 1, y - 1])
      return new_walls

    def only_one_path(x, y):
      north = 0 if self.grid[y + 1][x] == '#' else 1
      south = 0 if self.grid[y - 1][x] == '#' else 1
      east = 0 if self.grid[y][x + 1] == '#' else 1
      west = 0 if self.grid[y][x - 1] == '#' else 1
      return (north + south + east + west) == 1

    def carve_maze():
      # Start with a grid full of walls.
      # Pick a cell, mark it as part of the maze.
      self.grid[1][1] = '.'

      # Add the walls of the cell to the wall list.
      wall_list = [[1, 2], [2, 1]]

      # While there are walls in the list:
      while len(wall_list):

        # Pick a random wall from the list.
        random_wall = random.choice(wall_list)
        # If only one of the cells that the wall divides is visited,
        if only_one_path(random_wall[0], random_wall[1]):
          # Make the wall a passage and mark the unvisited cell as part of the maze.
          self.grid[random_wall[0]][random_wall[1]] = '.'
          # Add the neighboring walls of the cell to the wall list.
          new_walls = add_new_walls(random_wall[0], random_wall[1])                        # IT'S ADDING DUPES!
          for wall in new_walls:
            wall_list.append(wall)
        # Remove the wall from the list.
        wall_list.remove(random_wall)
        print(random_wall, wall_list)
      return self.grid

    self.maze = carve_maze()



  def print_grid(self):
    for row in self.maze:
      print(row)
      print()


new_maze = Maze(10)

new_maze.print_grid()