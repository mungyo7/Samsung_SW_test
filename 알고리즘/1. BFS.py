"""
1. 아이디어 
- 2중 for문 -> 값 1, 방문 x -> BFS
- BFS 돌면서 그림개수 +1, 최대값 갱신

2. 시간 복잡도
- O(V+E)

3. 자료구조
- 그래프 전체 : int[][]
- 방문 : bool[][]
- queue

https://www.acmicpc.net/problem/1926
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
"""

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

cnt = 0
maxv = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def bfs(y, x):
    rs = 1
    q= [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map [ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)