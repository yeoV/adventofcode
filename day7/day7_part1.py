# https://adventofcode.com/2024/day/7
import sys

read = sys.stdin.readlines
equations = list()
for line in read():
    k, v = line.rstrip().split(":")
    equations.append([int(k), list(map(int, v.split()))])


def run(target, values, current, depth):

    if depth == len(values) - 1:
        return target == current
    # operator *
    if run(target, values, current * values[depth + 1], depth + 1):
        return True
    # operator +
    if run(target, values, current + values[depth + 1], depth + 1):
        return True

    return False


res = 0
for equation in equations:
    target, values = equation[0], equation[1]
    if run(target, values, values[0], 0):
        res += target
print(res)
