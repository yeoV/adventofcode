#https://adventofcode.com/2024/day/4
import sys
from collections import deque

read = sys.stdin.readlines
graph = [list(line.strip()) for line in read()]
N, M = len(graph), len(graph[0])
directions = ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1))
WORD = "XMAS"
result = 0


def run(x, y):
    global result
    local_visited = set()
    q = deque([(x, y, 0, dx, dy) for dx, dy in directions])
    while q:
        x, y, idx, dx, dy = q.popleft()

        # 글자 완성
        if idx == len(WORD) - 1:
            result += 1
            continue

        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in local_visited:
            if WORD[idx + 1] == graph[nx][ny]:
                q.append((nx, ny, idx + 1, dx, dy))
                local_visited.add((nx, ny))


for x in range(N):
    for y in range(M):
        if graph[x][y] == "X":
            run(x, y)

print(result)
