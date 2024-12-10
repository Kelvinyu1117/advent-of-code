def part1(line):
  j = 0
  arr = []

  for i in range(0, len(line), 2):
    block_num = int(line[i])
    arr.extend([str(j) for block in range(0, block_num)])
    if i != len(line) - 1:
      free_space = int(line[i + 1])
      arr.extend(['.' for block in range(0, free_space)])
    j += 1

  n = len(arr)
  i = 0
  j = n - 1

  while i < j:
    while i < n and arr[i] != '.':
      i += 1

    while j >= 0 and arr[j] == '.':
      j -= 1

    arr[i] = arr[j]
    arr[j] = '.'
    i += 1
    j -= 1

  i = 0
  j = n - 1
  while i < j:
    while i < n and arr[i] != '.':
      i += 1

    while j >= 0 and arr[j] == '.':
        j -= 1

    arr[i] = arr[j]
    arr[j] = '.'
    i += 1
    j -= 1

  print(sum([i * int(c) for i, c in enumerate(arr) if c != '.']))

with open('input.txt', 'r') as f:
  part1(f.readline().strip())  
