import itertools



def part1(lines):
  def generate_operator_combinations(n):
    operators = ['*', '+']
    return list(itertools.product(operators, repeat=n))

  def evaluate_expression(lst, operators):
      result = lst[0]
      for i in range(1, len(lst)):
          if operators[i - 1] == '*':
              result *= lst[i]
          elif operators[i - 1] == '+':
              result += lst[i]
      return result

  def try_evaluate(target_sum, nums, operators):
    results = [evaluate_expression(nums, ops) for ops in operators]
    return target_sum in results

  mp = {}
  
  sum = 0
  for line in lines:
    tokens = line.split(': ')
    target_sum = int(tokens[0])
    nums = [int(n) for n in tokens[1].strip().split(' ')]
    
    n_ops = len(nums) - 1
    if not n_ops in mp:
      mp[n_ops] = generate_operator_combinations(n_ops)
    else:
      pass
    
    if try_evaluate(target_sum, nums, mp[n_ops]):
        sum += target_sum
    else:
      pass

  print(sum)


def part2(lines):
  def generate_operator_combinations(n):
    operators = ['*', '+', '||']
    return list(itertools.product(operators, repeat=n))

  def evaluate_expression(lst, operators):
    if lst == [] or operators == []: return 0
    result = lst[0]
    for i in range(1, len(lst)):
      if operators[i - 1] == '*':
          result *= lst[i]
      elif operators[i - 1] == '+':
          result += lst[i]
      elif operators[i - 1] == '||':
          result = int(str(result) + str(lst[i]))

    return result

  def try_evaluate(target, nums, operators):
    for ops in operators:
      if evaluate_expression(nums, ops) == target:
        return True

    return False

  mp = {}
  
  sum = 0
  for line in lines:
    tokens = line.split(': ')
    target = int(tokens[0])
    nums = [int(n) for n in tokens[1].strip().split(' ')]
    
    n_ops = len(nums) - 1
    if not n_ops in mp:
      mp[n_ops] = generate_operator_combinations(n_ops)
    else:
      pass
    
    if try_evaluate(target, nums, mp[n_ops]):
        sum += target
    else:
      pass

  print(sum)

with open('input.txt', 'r') as f:
  lines = [line.strip() for line in f.readlines()]
  part1(lines)
  part2(lines)
