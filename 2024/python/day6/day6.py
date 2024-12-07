def find_starting_point(grid):
  for i in range(0, len(grid)):
      for j in range(0, len(grid)):
        if grid[i][j] == '^':
          return (i, j)

def part1(grid):
  (i, j) = find_starting_point(grid)

  dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  dir_i = 0
  cnt = 1
  grid[i][j] = 'X'


  while i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
    if grid[i][j] == '.':
      cnt += 1
      grid[i][j] = 'X'
    elif grid[i][j] == '#':
      i -= dir[dir_i][0]
      j -= dir[dir_i][1]
      dir_i = (dir_i + 1) % len(dir)
    else:
      pass
    i += dir[dir_i][0]
    j += dir[dir_i][1]

  print(cnt)

with open('input.txt', 'r') as f:
  grid = [list(line.strip()) for line in f.readlines()]
  part1(grid)
