"""
https://www.acmicpc.net/problem/14503

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

57


1. 전체 맵 만들기
- 0: 청소 x 빈칸
- 1: 벽
- 2: 청소 완료

- 0 : 북쪽
- 1 : 동쪽
- 2 : 남쪽
- 3 : 서쪽

2. 현재 칸 0이면 청소 후 2로 바꾸기

3. 주변 4칸 탐색 -> 모두 0이 아니면 후진 방향 벽인지 확인 -> 벽이 아니라면 한칸 후진

4. 주변 4칸 탐색 -> 빈칸이 존재하면 반시계 방향으로 회전 -> for 문 돌다가 앞의 칸이 0이면 전진 이동동

"""

N, M = map(int, input().split())
y, x, d = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(N)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]
cnt = 0


while True:
    sw = False
    if map[y][x] == 0:
        map[y][x] = 2
        cnt += 1
    for i in range(1,5): # 0->2103, 1->3210, 2->0321
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        if 0<=ny<N and 0<=nx<M:
            if map[ny][nx] == 0:
                d = (d-i+4)%4
                y = ny
                x = nx
                sw = True
                break
    if sw == False:
        ny = y - dy[d]
        nx = x - dx[d]
        if (map[ny][nx] == 1):
            break
        else:
            y = ny
            x = nx
            #d

print(cnt)