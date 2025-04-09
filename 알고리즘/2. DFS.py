"""

https://www.acmicpc.net/problem/2667

7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
N = int(input())
map = [list(map(int,input().strip())) for _ in range(N)]
chk = [[False]*N for _ in range(N)]

each = 0
result = []
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    global each
    each += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0<=nx<N: # 범위 까먹지 말기!!
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny,nx)


for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            each = 0
            dfs(j,i)
            result.append(each)

print(len(result))
for i in result:
    print(i)
