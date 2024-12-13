# Using Stack or Queue
import sys

read = sys.stdin.readlines
equations = list()
for line in read():
    k, v = line.rstrip().split(":")
    equations.append([int(k), list(map(int, v.split()))])


def run(target, values):
    stack = [(values[0], 0)]  # current, depth

    while stack:
        cur, depth = stack.pop()

        if depth == len(values) - 1:
            if target == cur:
                return True
            continue

        nxt_value = values[depth + 1]
        # + operator
        stack.append((cur + nxt_value, depth + 1))
        # * operator
        stack.append((cur * nxt_value, depth + 1))
        # || operator
        stack.append((int(str(cur) + str(nxt_value)), depth + 1))

    return False


res = sum([x[0] for x in equations if run(x[0], x[1])])
print(res)
