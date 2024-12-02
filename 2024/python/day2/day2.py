import itertools
import operator


def monotone_increasing(lst):
    pairs = zip(lst, lst[1:])
    return all(itertools.starmap(operator.lt, pairs))


def monotone_decreasing(lst):
    pairs = zip(lst, lst[1:])
    return all(itertools.starmap(operator.gt, pairs))


def monotone(lst):
    return monotone_increasing(lst) or monotone_decreasing(lst)


def is_safe(lst):
    diffs = [abs(lst[n] - lst[n - 1]) for n in range(1, len(lst))]
    return monotone(lst) and all([x >= 1 and x <= 3 for x in diffs])


def is_removable_safe(lst):
    if (is_safe(lst)):
        return True
    else:
        for i in range(0, len(lst)):
            tmp = lst[0:i] + lst[i + 1:]
            if is_safe(tmp):
                return True
            else:
                pass

        return False


def part1(lines):
    print(sum([is_safe([int(n) for n in line.split(' ')]) for line in lines]))


def part2(lines):
    print(sum([is_removable_safe([int(n) for n in line.split(' ')])
          for line in lines]))


with open('input.txt', 'r') as f:
    lines = f.readlines()
    part1(lines)
    part2(lines)
