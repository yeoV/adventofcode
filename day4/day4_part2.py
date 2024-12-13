import sys

read = sys.stdin.readlines
graph = [list(x.rstrip()) for x in read()]
N, M = len(graph), len(graph[0])


def is_valid_word(x, y, arrow):
    WORD = {"M", "S"}
    words = {graph[x + dx][y + dy] for dx, dy in arrow}
    return len(WORD & words) == 2


def run(x, y):
    directions = [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]
    return all(is_valid_word(x, y, arrow) for arrow in directions)


result = 0
for x in range(1, N - 1):
    for y in range(1, M - 1):
        if graph[x][y] == "A":
            result += 1 if run(x, y) else 0

print(result)
