import re

def mul(x, y):
  return x * y


def part1(lines):
  r = re.compile('mul\([0-9]*,[0-9]*\)')
  print(sum([sum(list(map(lambda x: eval(x), r.findall(line)))) for line in lines]))

def part2(lines):
  r = re.compile("don't\(\)|do\(\)|mul\([0-9]*,[0-9]*\)")

  def sim(line):
    global yes
    sum = 0
    for token in r.findall(line):
      if token == "don't()":
          yes = False
      elif token == 'do()':
          yes = True
      else:
        if yes:
          sum = sum + eval(token)
        else:
          pass

    return sum

  print(sum([sim(line) for line in lines]))

with open('input.txt', 'r') as f:
  lines = f.readlines()
  part1(lines)
  part2(lines)
  