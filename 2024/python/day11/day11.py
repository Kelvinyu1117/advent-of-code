def solve(nums, times):
  mp = {n: 1 for n in nums}
  for _ in range(0, times):
    mpp = {}
    tmp_map = dict(mp)
    for k, v in tmp_map.items():
      if k == 0:
        mpp.setdefault(1, 0)
        mpp[1] += v      
      elif len(str(k)) % 2 == 0:
        tmp = str(k)
        a = int(tmp[0:len(tmp) // 2])
        b = int(tmp[len(tmp) // 2:])
        mpp.setdefault(a, 0)
        mpp.setdefault(b, 0)
        mpp[a] += v
        mpp[b] += v
      else:
        mpp.setdefault(k * 2024, 0)
        mpp[k * 2024] += v
    mp = dict(mpp)

  print(sum(mp.values()))

with open('input.txt', 'r') as f:
  nums = [int(i) for i in f.readline().strip().split(' ')]
  solve(nums, 25)
  solve(nums, 75)
