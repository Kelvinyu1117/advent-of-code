import re
import numpy as np

def part1(lines):
  lines = np.array([list(line[:-1]) if "\n" == line[-1] else list(line) for line in lines])

  diags = [lines[::-1,:].diagonal(i) for i in range(-lines.shape[0]+1,lines.shape[1])]
  diags.extend(lines.diagonal(i) for i in range(lines.shape[1]-1,-lines.shape[0],-1))
  h = ["".join(line) for line in lines.tolist()]
  t = ["".join(line) for line in lines.transpose()]
  d = ["".join(line.tolist()) for line in diags]


  r1 = re.compile('XMAS')
  r2 = re.compile('SAMX')

  horizontal = sum([len(r1.findall(line)) + len(r2.findall(line)) for line in h])
  vertical = sum([len(r1.findall(line)) + len(r2.findall(line)) for line in t])
  diagonal = sum([len(r1.findall(line)) + len(r2.findall(line)) for line in d])

  print(horizontal + vertical + diagonal)

def part2(lines):
  def try_match(grid, i, j):
    n = len(grid)
    m = len(grid[0])
    # assume grid[i][j] == 'A',
    if i - 1 < 0 or i + 1 >= m or j - 1 < 0 or j + 1 >= n: return False
    
    patterns = ['MAS', 'SAM']
    r = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
    l = grid[i + 1][j - 1] + grid[i][j] + grid[i - 1][j + 1]

    if r in patterns and l in patterns: return True
    else: return False

  grid = [list(lines.strip()) for lines in lines]
  cnt = 0
  for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
      if grid[i][j] == 'A':
        if try_match(grid, i, j):
            cnt += 1
  print(cnt)
with open('input.txt', 'r') as f:
  part1(f.readlines())
