import sys
from collections import deque
read = sys.stdin.readlines
graph = [list(line.rstrip()) for line in read()]
N,M = len(graph), len(graph[0])
directions = [(-1,0), (0,1), (1,0), (0,-1)]
direct_map = {"^": 0, ">": 1, "v": 2, "<": 3}


def run(x, y, idx) -> int:
    # x, y, direction
    q = deque([(x, y, idx)])
    result = 1 # X 갯수
    while q:
        x, y, d = q.popleft()

        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        # 벽 밖으로 나감
        if not (0 <= nx < N and 0 <= ny < M):
            return result
        
        # 방향 전환
        if graph[nx][ny] == "#":
            q.append((x, y, (d + 1)% 4))
        else:
            if graph[nx][ny] != "X":
                graph[nx][ny] = "X"
                result += 1
            q.append((nx, ny, d))


for x in range(N):
    for y in range(M):
        if graph[x][y] in direct_map.keys():
            result = run(x, y, direct_map[graph[x][y]])
print(result)