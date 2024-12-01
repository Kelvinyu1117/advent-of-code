from collections import Counter
a = []
b = []


def part1(a, b):
    a = sorted(a)
    b = sorted(b)
    print(sum([abs(x - y) for x, y in zip(a, b)]))


def part2(a, b):
    freq = Counter(b)
    print(sum([x * freq[x] for x in a]))


with open('input.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        tokens = line.strip().split(' ')

        a.append(int(tokens[0]))
        b.append(int(tokens[-1]))

part1(a, b)
part2(a, b)
