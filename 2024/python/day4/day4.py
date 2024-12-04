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

with open('input.txt', 'r') as f:
  part1(f.readlines())
