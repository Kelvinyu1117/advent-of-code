def is_after(rules, n, lst):
  if lst == []: return True
  else:
    return all([i in rules[n]['after'] for i in lst])


def part1(lines):
  invalid_lines = []
  line_break = False
  rules = {}
  result = 0

  for line in lines:
    if(line == '\n'):
      line_break = True
      continue
    
    if not line_break:
      tokens = line.split('|')
      n1 = int(tokens[0])
      n2 = int(tokens[1])

      if not n1 in rules:
        rules[n1] = {'before': set(), 'after': set()}
      if not n2 in rules:
        rules[n2] = {'before': set(), 'after': set()}

      rules[n1]['after'].add(n2)
      rules[n2]['before'].add(n1)
    else:
      nums = [int(token) for token in line.split(',')]
      rr = [is_after(rules, nums[i], nums[i + 1:]) for i in range(0, len(nums))]
      if(all(rr)):
        result += nums[int((len(nums)/2))]
      else:
        invalid_lines.append(nums)

  print(result)
  return invalid_lines

with open('input.txt', 'r') as f:
  lines = f.readlines()
  invalid_lines = part1(lines)
  print(invalid_lines)
